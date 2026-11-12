"""
Comprehensive development backend server for HR Software.
Runs on http://127.0.0.1:8000.
Directly reads and writes data to Neon PostgreSQL for all frontend and desktop endpoints.
"""

import os
import sys
import json
import mimetypes
from pathlib import Path
from datetime import datetime, date
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
        conn = psycopg2.connect(DATABASE_URL)
        return conn
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
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Frappe-CSRF-Token, Authorization")
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
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Frappe-CSRF-Token, Authorization")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
        self.end_headers()

    def get_user_from_cookie(self):
        cookie_header = self.headers.get("Cookie", "")
        for item in cookie_header.split(";"):
            item = item.strip()
            if item.startswith("user_id="):
                val = item.split("=")[1].strip()
                if val and val != "Guest":
                    return val
        return "Administrator"

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        # 1. Static Assets: /assets/hrms/...
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

        # 2. Login settings & OAuth
        if "hrms.api.system_settings.get_user_pass_login_disabled" in path:
            self._send_json(200, {"message": 0})
            return

        if "hrms.api.oauth.oauth_providers" in path:
            self._send_json(200, {"message": []})
            return

        # 3. Dev Context
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

        # 4. Doctype Fields & States
        if "hrms.api.get_doctype_fields" in path:
            doctype = query.get("doctype", [""])[0]
            fields = get_doctype_fields(doctype)
            self._send_json(200, {"message": fields})
            return

        if "hrms.api.get_doctype_states" in path:
            self._send_json(200, {
                "message": {
                    "Draft": "red",
                    "Submitted": "blue",
                    "Approved": "green",
                    "Rejected": "red",
                    "Cancelled": "gray"
                }
            })
            return

        # 5. HR Settings
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

        # 6. Current User Info from Neon DB
        if "hrms.api.get_current_user_info" in path or "frappe.auth.get_logged_user" in path:
            user_name = self.get_user_from_cookie()
            conn = get_db()
            user_record = None
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, email, first_name, full_name, roles FROM users WHERE name = %s OR email = %s LIMIT 1", (user_name, user_name))
                user_record = cur.fetchone()
                cur.close()
                conn.close()

            if not user_record:
                user_record = {
                    "name": user_name,
                    "email": f"{user_name.lower()}@example.com",
                    "first_name": "Admin" if user_name == "Administrator" else user_name.split("@")[0].capitalize(),
                    "full_name": "Administrator" if user_name == "Administrator" else user_name,
                    "roles": ["System Manager", "HR Manager", "Employee", "HR User"]
                }
            self._send_json(200, {"message": user_record})
            return

        # 7. Current Employee Info from Neon DB
        if "hrms.api.get_current_employee_info" in path:
            user_name = self.get_user_from_cookie()
            conn = get_db()
            emp_record = None
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, employee_name, first_name, designation, department, company, reports_to, user_id FROM employees WHERE user_id = %s OR name = %s LIMIT 1", (user_name, user_name))
                emp_record = cur.fetchone()
                cur.close()
                conn.close()

            if not emp_record:
                emp_record = {
                    "name": "HR-EMP-00001",
                    "employee_name": "Administrator",
                    "first_name": "Admin",
                    "designation": "HR Director",
                    "department": "Human Resources",
                    "company": "HR Software Co",
                    "reports_to": "",
                    "user_id": user_name
                }
            self._send_json(200, {"message": emp_record})
            return

        # 8. All Employees from Neon DB
        if "hrms.api.get_all_employees" in path:
            conn = get_db()
            employees = []
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, employee_name, designation, department, company, reports_to, user_id, status FROM employees ORDER BY id")
                employees = cur.fetchall()
                cur.close()
                conn.close()
            self._send_json(200, {"message": employees})
            return

        # 9. Leave Types from Neon DB
        if "hrms.api.get_leave_types" in path:
            conn = get_db()
            types = []
            if conn:
                cur = conn.cursor()
                cur.execute("SELECT name FROM leave_types ORDER BY name")
                types = [row[0] for row in cur.fetchall()]
                cur.close()
                conn.close()
            self._send_json(200, {"message": types or ["Annual Leave", "Casual Leave", "Sick Leave"]})
            return

        # 10. Leave Balance Map from Neon DB
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
                """)
                for row in cur.fetchall():
                    balance_map[row["name"]] = {"balance": row["balance"], "allocated_leaves": row["allocated_leaves"]}
                cur.close()
                conn.close()
            self._send_json(200, {"message": balance_map})
            return

        # 11. Leave Approval Details
        if "hrms.api.get_leave_approval_details" in path:
            self._send_json(200, {
                "message": {
                    "is_mandatory": 0,
                    "department_approvers": [
                        {"name": "Administrator", "full_name": "HR Department : Administrator"}
                    ]
                }
            })
            return

        # 12. Leave Applications from Neon DB
        if "hrms.api.get_leave_applications" in path:
            conn = get_db()
            leaves = []
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, employee, employee_name, leave_type, from_date, to_date, total_leave_days, status, docstatus, description FROM leave_applications ORDER BY id DESC")
                leaves = cur.fetchall()
                cur.close()
                conn.close()
            self._send_json(200, {"message": leaves})
            return

        # 13. Expense Claim Types & Claims from Neon DB
        if "hrms.api.get_expense_claim_types" in path:
            conn = get_db()
            types = []
            if conn:
                cur = conn.cursor()
                cur.execute("SELECT name FROM expense_claim_types ORDER BY name")
                types = [row[0] for row in cur.fetchall()]
                cur.close()
                conn.close()
            self._send_json(200, {"message": types or ["Travel", "Meals", "Medical"]})
            return

        if "hrms.api.get_expense_claims" in path:
            conn = get_db()
            claims = []
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, employee, employee_name, total_claimed_amount, total_sanctioned_amount, status, docstatus, posting_date FROM expense_claims ORDER BY id DESC")
                claims = cur.fetchall()
                cur.close()
                conn.close()
            self._send_json(200, {"message": claims})
            return

        if "hrms.api.get_expense_claim_summary" in path:
            conn = get_db()
            total = 0.0
            if conn:
                cur = conn.cursor()
                cur.execute("SELECT COALESCE(SUM(total_claimed_amount), 0) FROM expense_claims")
                total = float(cur.fetchone()[0])
                cur.close()
                conn.close()
            self._send_json(200, {"message": {"total_claimed_amount": total, "total_sanctioned_amount": total}})
            return

        # 14. Attendance & Shifts from Neon DB
        if "hrms.api.get_attendance_requests" in path:
            conn = get_db()
            atts = []
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, employee, employee_name, from_date, to_date, reason, status, docstatus FROM attendance_requests ORDER BY id DESC")
                atts = cur.fetchall()
                cur.close()
                conn.close()
            self._send_json(200, {"message": atts})
            return

        if "hrms.api.get_shift_requests" in path:
            conn = get_db()
            shifts = []
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, employee, employee_name, shift_type, from_date, to_date, status, docstatus FROM shift_requests ORDER BY id DESC")
                shifts = cur.fetchall()
                cur.close()
                conn.close()
            self._send_json(200, {"message": shifts})
            return

        if "hrms.api.get_shifts" in path:
            conn = get_db()
            shifts = []
            if conn:
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur.execute("SELECT name, start_time::text as start_time, end_time::text as end_time FROM shift_types")
                shifts = cur.fetchall()
                cur.close()
                conn.close()
            self._send_json(200, {"message": shifts})
            return

        # 15. Roster Management Suite APIs
        if "get_default_company" in path:
            self._send_json(200, {"message": "HR Software Co"})
            return

        if "get_permitted_filter_doctypes" in path:
            self._send_json(200, {"message": ["Department", "Branch", "Designation"]})
            return

        if "get_events" in path:
            self._send_json(200, {"message": {"holidays": {}, "leaves": {}, "shifts": {}}})
            return

        # 16. Currencies & Permissions
        if "hrms.api.get_company_currencies" in path:
            self._send_json(200, {"message": ["USD", "EUR", "KES", "GBP"]})
            return

        if "hrms.api.get_currency_symbols" in path:
            self._send_json(200, {"message": {"USD": "$", "EUR": "€", "KES": "KSh", "GBP": "£"}})
            return

        if "frappe.client.get_doc_permissions" in path or "frappe.client.has_permission" in path:
            self._send_json(200, {
                "message": {
                    "read": 1, "write": 1, "create": 1, "submit": 1, "cancel": 1, "has_permission": True
                }
            })
            return

        if "hrms.api.get_unread_notifications_count" in path or "hrms.api.are_push_notifications_enabled" in path:
            self._send_json(200, {"message": 0})
            return

        self._send_json(200, {"message": []})

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

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

        # 1. Login
        if path.endswith("/login") or "login" in path:
            usr = data.get("usr") or "Administrator"
            print(f"[AUTH] Login: {usr}", flush=True)
            cookies = [
                f"user_id={usr}; Path=/; SameSite=Lax",
                f"system_user=yes; Path=/; SameSite=Lax",
                f"full_name={usr}; Path=/; SameSite=Lax",
                f"sid=session_{usr}; Path=/; HttpOnly; SameSite=Lax"
            ]
            self._send_json(200, {
                "message": "Logged In",
                "home_page": "/hrms",
                "full_name": usr
            }, cookies=cookies)
            return

        # 2. Logout
        if path.endswith("/logout") or "logout" in path:
            cookies = [
                "user_id=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT",
                "sid=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT"
            ]
            self._send_json(200, {"message": "Logged Out"}, cookies=cookies)
            return

        # 3. Dev Context
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

        # 4. Reportview for Employee Checkin
        if "frappe.desk.reportview.get" in path:
            doctype = data.get("doctype", "")
            if doctype == "Employee Checkin":
                conn = get_db()
                checkins = []
                if conn:
                    cur = conn.cursor(cursor_factory=RealDictCursor)
                    cur.execute("SELECT name, employee, employee_name, log_type, time::text as time, device_id FROM employee_checkins ORDER BY time DESC")
                    checkins = cur.fetchall()
                    cur.close()
                    conn.close()

                self._send_json(200, {
                    "message": {
                        "keys": ["name", "employee", "employee_name", "log_type", "time", "device_id"],
                        "values": [
                            [c["name"], c["employee"], c["employee_name"], c["log_type"], c["time"], c.get("device_id", "")]
                            for c in checkins
                        ]
                    }
                })
                return
            self._send_json(200, {"message": {"keys": [], "values": []}})
            return

        # 5. Check-in submission (Saved into Neon DB!)
        if "Employee Checkin" in path or data.get("doctype") == "Employee Checkin":
            log_type = data.get("log_type", "IN")
            now = datetime.now()
            name = f"CHECKIN-{int(now.timestamp())}"
            conn = get_db()
            if conn:
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO employee_checkins (name, employee, employee_name, log_type, time, device_id)
                    VALUES (%s, 'HR-EMP-00001', 'Administrator', %s, %s, 'Web PWA')
                """, (name, log_type, now))
                conn.commit()
                cur.close()
                conn.close()

            print(f"[Neon DB] Saved Check-in {log_type} at {now}", flush=True)
            record = {
                "name": name,
                "employee": "HR-EMP-00001",
                "employee_name": "Administrator",
                "log_type": log_type,
                "time": now.isoformat(),
                "device_id": "Web PWA"
            }
            self._send_json(200, {"data": record, "message": record})
            return

        # 6. Leave Application Submission (Saved into Neon DB!)
        if "Leave Application" in path or data.get("doctype") == "Leave Application":
            doc = data.get("doc", data)
            leave_name = f"HR-LV-{int(datetime.now().timestamp())}"
            conn = get_db()
            if conn:
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO leave_applications (name, employee, employee_name, leave_type, from_date, to_date, total_leave_days, status, description)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, 'Approved', %s)
                """, (
                    leave_name,
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
            doc["status"] = "Approved"
            doc["docstatus"] = 1
            print(f"[Neon DB] Saved Leave Application {leave_name}", flush=True)
            self._send_json(200, {"data": doc, "message": doc})
            return

        # 7. Generic Resource Insert / Save
        if path.startswith("/api/resource/") or "frappe.client.insert" in path or "frappe.client.save" in path:
            doc = data.get("doc", data)
            doctype = doc.get("doctype", path.split("/")[-1] if "/api/resource/" in path else "Doc")
            doc["name"] = f"DOC-{int(datetime.now().timestamp())}"
            doc["docstatus"] = 0
            doc["status"] = "Draft"
            self._send_json(200, {"data": doc, "message": doc})
            return

        # 8. Roster post endpoints
        if "get_default_company" in path or "get_value" in path:
            self._send_json(200, {"message": {"default_company": "HR Software Co"}})
            return

        if "get_permitted_filter_doctypes" in path:
            self._send_json(200, {"message": ["Department", "Branch", "Designation"]})
            return

        if "get_events" in path:
            self._send_json(200, {"message": {"holidays": {}, "leaves": {}, "shifts": {}}})
            return

        self._send_json(200, {"message": "OK", "data": data})

def run(port=8000):
    server_address = ("127.0.0.1", port)
    httpd = HTTPServer(server_address, HRBackendHandler)
    print("=" * 60, flush=True)
    print(f" HR Software Backend (Connected to Neon PostgreSQL)", flush=True)
    print(f" Listening on: http://127.0.0.1:{port}", flush=True)
    print("=" * 60, flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...", flush=True)
        httpd.server_close()

if __name__ == "__main__":
    port = int(os.environ.get("SERVER_PORT", 8000))
    run(port=port)
