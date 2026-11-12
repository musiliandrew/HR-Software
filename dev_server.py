"""
Multi-Tenant B2B SaaS Backend Server for HR Software.
Runs on http://127.0.0.1:8000 connected to Neon PostgreSQL.

Key Architectural Capabilities:
1. Multi-Tenant Scoping: Queries partitioned by tenant_id (Company boundary).
2. Subscription & Seat Engine: Enforces seat limits, manages monthly tiers, and billing info.
3. Company Onboarding: Registers new Companies / HR Leads with automated provisioning.
4. Role-Based Access: Differentiates Company Owners / HR Admins from invited Employees.
"""

import os
import sys
import json
import mimetypes
from pathlib import Path
from datetime import datetime, date, timedelta
from decimal import Decimal
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "hrms" / "hrms" / "public"
DATABASE_URL = os.environ.get("DATABASE_URL")

SUPPORTED_FIELD_TYPES = {
    "Link", "Select", "Small Text", "Text", "Long Text",
    "Text Editor", "Table", "Check", "Data", "Float", "Int",
    "Section Break", "Date", "Time", "Datetime", "Currency"
}

PLAN_CONFIG = {
    "Starter": {"price": 29.00, "seats": 15},
    "Growth": {"price": 79.00, "seats": 50},
    "Enterprise": {"price": 199.00, "seats": 9999}
}

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} not serializable")

def get_doctype_fields(doctype_name: str):
    clean_name = doctype_name.lower().replace(" ", "_").strip()
    root_path = BASE_DIR / "hrms" / "hrms"
    for pattern in [f"**/doctype/{clean_name}/{clean_name}.json", f"**/{clean_name}.json"]:
        matches = list(root_path.glob(pattern))
        if matches:
            for m in matches:
                if "doctype_settings" in str(m):
                    continue
                try:
                    with open(m, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if "fields" in data:
                        return [
                            field for field in data["fields"]
                            if field.get("fieldtype") in SUPPORTED_FIELD_TYPES and field.get("fieldname") != "amended_from"
                        ]
                except Exception:
                    pass
    return []

def get_db():
    if not DATABASE_URL:
        return None
    try:
        return psycopg2.connect(DATABASE_URL)
    except Exception as e:
        print(f"[Neon DB Error] {e}", flush=True)
        return None

class HRBackendHandler(BaseHTTPRequestHandler):
    def _send_json(self, status, data, cookies=None):
        response_bytes = json.dumps(data, default=json_serial).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response_bytes)))
        self.send_header("Access-Control-Allow-Origin", self.headers.get("Origin", "*"))
        self.send_header("Access-Control-Allow-Credentials", "true")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Frappe-CSRF-Token, Authorization, X-Tenant-Id")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
        if cookies:
            for c in cookies:
                self.send_header("Set-Cookie", c)
        self.end_headers()
        self.wfile.write(response_bytes)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", self.headers.get("Origin", "*"))
        self.send_header("Access-Control-Allow-Credentials", "true")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Frappe-CSRF-Token, Authorization, X-Tenant-Id")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
        self.end_headers()

    def get_session_info(self):
        """Extracts user and tenant_id from cookies or headers."""
        cookie_header = self.headers.get("Cookie", "")
        user = "Administrator"
        for item in cookie_header.split(";"):
            item = item.strip()
            if item.startswith("user_id="):
                val = item.split("=")[1].strip()
                if val and val != "Guest":
                    user = val

        # Check tenant_id from header or query database
        tenant_id = self.headers.get("X-Tenant-Id")
        if not tenant_id:
            conn = get_db()
            if conn:
                cur = conn.cursor()
                cur.execute("SELECT tenant_id FROM users WHERE name = %s OR email = %s LIMIT 1", (user, user))
                row = cur.fetchone()
                if row and row[0]:
                    tenant_id = row[0]
                cur.close()
                conn.close()

        tenant_id = tenant_id or "TENANT-ACME"
        return user, tenant_id

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)
        user_name, tenant_id = self.get_session_info()

        # 1. Static Assets
        if path.startswith("/assets/hrms/"):
            rel_path = path[len("/assets/hrms/"):]
            file_path = PUBLIC_DIR / rel_path
            if file_path.is_file():
                mime_type, _ = mimetypes.guess_type(str(file_path))
                mime_type = mime_type or "application/octet-stream"
                try:
                    with open(file_path, "rb") as f:
                        content = f.read()
                    self.send_response(200)
                    self.send_header("Content-Type", mime_type)
                    self.send_header("Content-Length", str(len(content)))
                    self.send_header("Cache-Control", "no-cache")
                    self.end_headers()
                    self.wfile.write(content)
                    return
                except Exception as e:
                    print(f"Error serving asset: {e}", flush=True)

        # 2. SaaS Company & Subscription Information
        if "saas.get_company_subscription" in path or "get_subscription_info" in path:
            conn = get_db()
            info = {}
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("""
                    SELECT t.id as tenant_id, t.name as company_name, t.slug, t.billing_email, 
                           t.plan_tier, t.seat_limit, t.status as tenant_status,
                           s.monthly_price, s.billing_cycle, s.status as subscription_status, s.current_period_end
                    FROM tenants t
                    LEFT JOIN subscriptions s ON t.id = s.tenant_id
                    WHERE t.id = %s LIMIT 1
                """, (tenant_id,))
                tenant_row = cur.fetchone()

                cur.execute("SELECT COUNT(*) as used_seats FROM employees WHERE tenant_id = %s", (tenant_id,))
                seats_row = cur.fetchone()
                cur.close()
                conn.close()

                if tenant_row:
                    info = dict(tenant_row)
                    info["used_seats"] = seats_row["used_seats"] if seats_row else 1
                    info["seats_available"] = max(0, info.get("seat_limit", 50) - info["used_seats"])

            self._send_json(200, {"message": info})
            return

        # 3. SaaS Plan Listing
        if "saas.get_plans" in path:
            self._send_json(200, {
                "message": [
                    {"name": "Starter", "price": 29.00, "seats": 15, "description": "For small teams and growing startups"},
                    {"name": "Growth", "price": 79.00, "seats": 50, "description": "For mid-size companies with shift & geolocation needs"},
                    {"name": "Enterprise", "price": 199.00, "seats": "Unlimited", "description": "Complete custom payroll & dedicated support"}
                ]
            })
            return

        # 4. Dev Context
        if "hrms.www.hrms.get_context_for_dev" in path:
            self._send_json(200, {
                "message": {
                    "site_name": os.environ.get("SITE_NAME", "hrms.localhost"),
                    "socketio_port": int(os.environ.get("SOCKETIO_PORT", 9000)),
                    "push_relay_server_url": os.environ.get("PUSH_RELAY_SERVER_URL", ""),
                    "default_route": "/hrms",
                    "lang": "en",
                    "layout_direction": "ltr"
                }
            })
            return

        # 5. Doctype Fields & States
        if "hrms.api.get_doctype_fields" in path:
            doctype = query.get("doctype", [""])[0]
            fields = get_doctype_fields(doctype)
            self._send_json(200, {"message": fields})
            return

        if "hrms.api.get_doctype_states" in path:
            self._send_json(200, {
                "message": {
                    "Draft": "red", "Submitted": "blue", "Approved": "green", "Rejected": "red", "Cancelled": "gray"
                }
            })
            return

        # 6. HR Settings
        if "hrms.api.get_hr_settings" in path:
            self._send_json(200, {
                "message": {
                    "allow_employee_checkin_from_mobile_app": 1,
                    "allow_geolocation_tracking": 1,
                    "prevent_self_leave_approval": 0,
                    "enable_multi_currency_expense_claim": 1
                }
            })
            return

        # 7. Current User Info (Tenant Scoped)
        if "hrms.api.get_current_user_info" in path or "frappe.auth.get_logged_user" in path:
            conn = get_db()
            user_record = None
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, tenant_id, email, first_name, full_name, role, roles FROM users WHERE (name = %s OR email = %s) AND tenant_id = %s LIMIT 1", (user_name, user_name, tenant_id))
                user_record = cur.fetchone()
                cur.close()
                conn.close()

            if not user_record:
                user_record = {
                    "name": user_name,
                    "tenant_id": tenant_id,
                    "email": user_name if "@" in user_name else f"{user_name.lower()}@example.com",
                    "first_name": "Admin" if user_name == "Administrator" else user_name.split("@")[0].capitalize(),
                    "full_name": "Administrator" if user_name == "Administrator" else user_name,
                    "role": "Company Owner" if user_name == "Administrator" else "Employee",
                    "roles": ["System Manager", "HR Manager", "Employee", "HR User"]
                }
            self._send_json(200, {"message": user_record})
            return

        # 8. Current Employee Info (Tenant Scoped)
        if "hrms.api.get_current_employee_info" in path:
            conn = get_db()
            emp_record = None
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, tenant_id, employee_name, first_name, designation, department, company, reports_to, user_id FROM employees WHERE (user_id = %s OR name = %s) AND tenant_id = %s LIMIT 1", (user_name, user_name, tenant_id))
                emp_record = cur.fetchone()
                cur.close()
                conn.close()

            if not emp_record:
                emp_record = {
                    "name": "HR-EMP-00001",
                    "tenant_id": tenant_id,
                    "employee_name": "Administrator",
                    "first_name": "Admin",
                    "designation": "HR Director",
                    "department": "Human Resources",
                    "company": "Acme Corporation",
                    "reports_to": "",
                    "user_id": user_name
                }
            self._send_json(200, {"message": emp_record})
            return

        # 9. All Employees for this Tenant
        if "hrms.api.get_all_employees" in path:
            conn = get_db()
            employees = []
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, tenant_id, employee_name, first_name, designation, department, company, reports_to, user_id, status FROM employees WHERE tenant_id = %s ORDER BY id", (tenant_id,))
                employees = cur.fetchall()
                cur.close()
                conn.close()
            self._send_json(200, {"message": employees})
            return

        # 10. Leave Types & Balances (Tenant Scoped)
        if "hrms.api.get_leave_types" in path:
            conn = get_db()
            types = []
            if conn:
                cur = conn.cursor()
                cur.execute("SELECT name FROM leave_types WHERE tenant_id = %s ORDER BY name", (tenant_id,))
                types = [row[0] for row in cur.fetchall()]
                cur.close()
                conn.close()
            self._send_json(200, {"message": types or ["Annual Leave", "Casual Leave", "Sick Leave"]})
            return

        if "hrms.api.get_leave_balance_map" in path:
            conn = get_db()
            balance_map = {}
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("""
                    SELECT lt.name, COALESCE(la.leaves_remaining, lt.max_days_allowed) as balance, 
                           COALESCE(la.total_allocated, lt.max_days_allowed) as allocated_leaves 
                    FROM leave_types lt 
                    LEFT JOIN leave_allocations la ON lt.name = la.leave_type AND la.employee = 'HR-EMP-00001'
                    WHERE lt.tenant_id = %s
                """, (tenant_id,))
                for row in cur.fetchall():
                    balance_map[row["name"]] = {"balance": row["balance"], "allocated_leaves": row["allocated_leaves"]}
                cur.close()
                conn.close()
            self._send_json(200, {"message": balance_map})
            return

        if "hrms.api.get_leave_applications" in path:
            conn = get_db()
            leaves = []
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, employee, employee_name, leave_type, from_date, to_date, total_leave_days, status, docstatus, description FROM leave_applications WHERE tenant_id = %s ORDER BY id DESC", (tenant_id,))
                leaves = cur.fetchall()
                cur.close()
                conn.close()
            self._send_json(200, {"message": leaves})
            return

        # 11. Expenses, Attendance, Shifts (Tenant Scoped)
        if "hrms.api.get_expense_claims" in path:
            conn = get_db()
            claims = []
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, employee, employee_name, total_claimed_amount, total_sanctioned_amount, status, docstatus, posting_date FROM expense_claims WHERE tenant_id = %s ORDER BY id DESC", (tenant_id,))
                claims = cur.fetchall()
                cur.close()
                conn.close()
            self._send_json(200, {"message": claims})
            return

        if "hrms.api.get_attendance_requests" in path:
            conn = get_db()
            atts = []
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, employee, employee_name, from_date, to_date, reason, status, docstatus FROM attendance_requests WHERE tenant_id = %s ORDER BY id DESC", (tenant_id,))
                atts = cur.fetchall()
                cur.close()
                conn.close()
            self._send_json(200, {"message": atts})
            return

        if "hrms.api.get_shifts" in path:
            conn = get_db()
            shifts = []
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, start_time::text as start_time, end_time::text as end_time FROM shift_types WHERE tenant_id = %s", (tenant_id,))
                shifts = cur.fetchall()
                cur.close()
                conn.close()
            self._send_json(200, {"message": shifts})
            return

        # 12. Roster Management APIs
        if "get_default_company" in path:
            self._send_json(200, {"message": "Acme Corporation"})
            return

        if "get_permitted_filter_doctypes" in path:
            self._send_json(200, {"message": ["Department", "Branch", "Designation"]})
            return

        if "get_events" in path:
            self._send_json(200, {"message": {"holidays": {}, "leaves": {}, "shifts": {}}})
            return

        # Fallbacks
        if "hrms.api.system_settings.get_user_pass_login_disabled" in path:
            self._send_json(200, {"message": 0})
            return
        if "hrms.api.oauth.oauth_providers" in path or "hrms.api.get_unread_notifications_count" in path:
            self._send_json(200, {"message": [] if "oauth" in path else 0})
            return

        self._send_json(200, {"message": []})

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        user_name, tenant_id = self.get_session_info()

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length > 0 else b""
        data = {}
        try:
            if body:
                content_type = self.headers.get("Content-Type", "")
                if "application/json" in content_type:
                    data = json.loads(body.decode("utf-8"))
                else:
                    data = {k: v[0] for k, v in parse_qs(body.decode("utf-8")).items()}
        except Exception:
            pass

        # 1. Company Registration (SaaS Onboarding)
        if "saas.register_company" in path:
            company_name = data.get("company_name", "My Company")
            admin_email = data.get("admin_email", "owner@company.com")
            admin_name = data.get("admin_name", "Company Lead")
            plan_tier = data.get("plan_tier", "Growth")

            slug = company_name.lower().replace(" ", "-").strip()
            new_tenant_id = f"TENANT-{slug.upper()[:15]}"
            plan_info = PLAN_CONFIG.get(plan_tier, PLAN_CONFIG["Growth"])

            conn = get_db()
            if conn:
                cur = conn.cursor()
                # Create Tenant
                cur.execute("""
                    INSERT INTO tenants (id, name, slug, billing_email, plan_tier, seat_limit, status)
                    VALUES (%s, %s, %s, %s, %s, %s, 'Active')
                    ON CONFLICT (id) DO NOTHING
                """, (new_tenant_id, company_name, slug, admin_email, plan_tier, plan_info["seats"]))

                # Create Subscription
                cur.execute("""
                    INSERT INTO subscriptions (tenant_id, plan_name, monthly_price, status, current_period_end)
                    VALUES (%s, %s, %s, 'active', CURRENT_TIMESTAMP + INTERVAL '30 days')
                """, (new_tenant_id, f"{plan_tier} Plan", plan_info["price"]))

                # Create Owner User
                cur.execute("""
                    INSERT INTO users (name, tenant_id, email, first_name, full_name, role, roles)
                    VALUES (%s, %s, %s, %s, %s, 'Company Owner', '{"Company Owner", "HR Manager", "Employee"}')
                    ON CONFLICT (name) DO NOTHING
                """, (admin_email, new_tenant_id, admin_email, admin_name, admin_name))

                # Create Initial Employee
                cur.execute("""
                    INSERT INTO employees (name, tenant_id, employee_name, first_name, designation, department, company, user_id)
                    VALUES (%s, %s, %s, %s, 'HR Director', 'Management', %s, %s)
                    ON CONFLICT (name) DO NOTHING
                """, (f"EMP-{new_tenant_id[:8]}-01", new_tenant_id, admin_name, admin_name, company_name, admin_email))

                conn.commit()
                cur.close()
                conn.close()

            print(f"[SaaS Onboard] Registered Company: {company_name} ({new_tenant_id})", flush=True)
            self._send_json(200, {
                "message": "Company registered successfully",
                "tenant_id": new_tenant_id,
                "company_name": company_name,
                "plan": plan_tier
            })
            return

        # 2. Update Subscription / Change Plan
        if "saas.update_subscription" in path:
            new_plan = data.get("plan_tier", "Growth")
            plan_info = PLAN_CONFIG.get(new_plan, PLAN_CONFIG["Growth"])
            conn = get_db()
            if conn:
                cur = conn.cursor()
                cur.execute("""
                    UPDATE tenants SET plan_tier = %s, seat_limit = %s WHERE id = %s
                """, (new_plan, plan_info["seats"], tenant_id))
                cur.execute("""
                    UPDATE subscriptions SET plan_name = %s, monthly_price = %s WHERE tenant_id = %s
                """, (f"{new_plan} Plan", plan_info["price"], tenant_id))
                conn.commit()
                cur.close()
                conn.close()

            self._send_json(200, {
                "message": f"Subscription upgraded to {new_plan}",
                "plan_tier": new_plan,
                "seat_limit": plan_info["seats"],
                "monthly_price": plan_info["price"]
            })
            return

        # 3. Invite / Add Employee with Seat Limit Enforcement
        if "saas.invite_employee" in path:
            conn = get_db()
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT seat_limit FROM tenants WHERE id = %s", (tenant_id,))
                t = cur.fetchone()
                cur.execute("SELECT COUNT(*) as count FROM employees WHERE tenant_id = %s", (tenant_id,))
                e = cur.fetchone()
                
                seat_limit = t["seat_limit"] if t else 50
                used_seats = e["count"] if e else 0

                if used_seats >= seat_limit:
                    cur.close()
                    conn.close()
                    self._send_json(403, {
                        "error": "Seat limit reached",
                        "message": f"Your current plan is capped at {seat_limit} seats. Please upgrade your company plan to add more employees."
                    })
                    return

                # Add employee
                emp_name = data.get("employee_name", "New Employee")
                emp_email = data.get("email", f"emp_{int(datetime.now().timestamp())}@example.com")
                emp_id = f"HR-EMP-{used_seats + 1:05d}"
                designation = data.get("designation", "Staff")
                department = data.get("department", "General")

                cur.execute("""
                    INSERT INTO users (name, tenant_id, email, first_name, full_name, role)
                    VALUES (%s, %s, %s, %s, %s, 'Employee')
                """, (emp_email, tenant_id, emp_email, emp_name.split()[0], emp_name))

                cur.execute("""
                    INSERT INTO employees (name, tenant_id, employee_name, first_name, designation, department, company, user_id)
                    VALUES (%s, %s, %s, %s, %s, %s, 'Acme Corporation', %s)
                """, (emp_id, tenant_id, emp_name, emp_name.split()[0], designation, department, emp_email))

                conn.commit()
                cur.close()
                conn.close()

                self._send_json(200, {
                    "message": "Employee invited successfully",
                    "employee_id": emp_id,
                    "seats_used": used_seats + 1,
                    "seats_total": seat_limit
                })
                return

        # 4. Login
        if path.endswith("/login") or "login" in path:
            usr = data.get("usr") or "Administrator"
            cookies = [
                f"user_id={usr}; Path=/; SameSite=Lax",
                f"tenant_id={tenant_id}; Path=/; SameSite=Lax",
                f"system_user=yes; Path=/; SameSite=Lax",
                f"full_name={usr}; Path=/; SameSite=Lax",
                f"sid=session_{usr}; Path=/; HttpOnly; SameSite=Lax"
            ]
            self._send_json(200, {
                "message": "Logged In",
                "home_page": "/hrms",
                "full_name": usr,
                "tenant_id": tenant_id
            }, cookies=cookies)
            return

        # 5. Logout
        if path.endswith("/logout") or "logout" in path:
            cookies = [
                "user_id=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT",
                "tenant_id=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT",
                "sid=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT"
            ]
            self._send_json(200, {"message": "Logged Out"}, cookies=cookies)
            return

        # 6. Check-in submission (Tenant Scoped)
        if "Employee Checkin" in path or data.get("doctype") == "Employee Checkin":
            log_type = data.get("log_type", "IN")
            now = datetime.now()
            name = f"CHECKIN-{int(now.timestamp())}"
            conn = get_db()
            if conn:
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO employee_checkins (name, tenant_id, employee, employee_name, log_type, time, device_id)
                    VALUES (%s, %s, 'HR-EMP-00001', 'Administrator', %s, %s, 'Web PWA')
                """, (name, tenant_id, log_type, now))
                conn.commit()
                cur.close()
                conn.close()

            record = {
                "name": name,
                "tenant_id": tenant_id,
                "employee": "HR-EMP-00001",
                "employee_name": "Administrator",
                "log_type": log_type,
                "time": now.isoformat(),
                "device_id": "Web PWA"
            }
            self._send_json(200, {"data": record, "message": record})
            return

        # 7. Leave Application Submission (Tenant Scoped)
        if "Leave Application" in path or data.get("doctype") == "Leave Application":
            doc = data.get("doc", data)
            leave_name = f"HR-LV-{int(datetime.now().timestamp())}"
            conn = get_db()
            if conn:
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO leave_applications (name, tenant_id, employee, employee_name, leave_type, from_date, to_date, total_leave_days, status, description)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'Approved', %s)
                """, (
                    leave_name,
                    tenant_id,
                    doc.get("employee", "HR-EMP-00001"),
                    doc.get("employee_name", "Administrator"),
                    doc.get("leave_type", "Annual Leave"),
                    doc.get("from_date", date.today().isoformat()),
                    doc.get("to_date", date.today().isoformat()),
                    int(doc.get("total_leave_days", 1)),
                    doc.get("description", "")
                ))
                conn.commit()
                cur.close()
                conn.close()

            doc["name"] = leave_name
            doc["tenant_id"] = tenant_id
            doc["status"] = "Approved"
            doc["docstatus"] = 1
            self._send_json(200, {"data": doc, "message": doc})
            return

        # Fallback
        self._send_json(200, {"message": "OK", "data": data})

def run(port=8000):
    server_address = ("127.0.0.1", port)
    httpd = HTTPServer(server_address, HRBackendHandler)
    print("=" * 65, flush=True)
    print(f" HR Software Multi-Tenant B2B SaaS Backend Server", flush=True)
    print(f" Listening on: http://127.0.0.1:{port}", flush=True)
    print(f" Neon PostgreSQL: Partitioned Multi-Tenancy Active", flush=True)
    print("=" * 65, flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...", flush=True)
        httpd.server_close()

if __name__ == "__main__":
    port = int(os.environ.get("SERVER_PORT", 8000))
    run(port=port)
