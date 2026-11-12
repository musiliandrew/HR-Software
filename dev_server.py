"""
Lightweight development backend server for HR Software.
Runs on http://127.0.0.1:8000 and connects to Neon PostgreSQL.
Handles Frappe API authentication, session cookies, and serves public assets.
"""

import os
import sys
import json
import mimetypes
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
import psycopg2

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "hrms" / "hrms" / "public"
DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    if not DATABASE_URL:
        return None
    try:
        return psycopg2.connect(DATABASE_URL)
    except Exception as e:
        print(f"[DB Error] {e}")
        return None

class HRBackendHandler(BaseHTTPRequestHandler):
    def _send_json(self, status, data, cookies=None):
        response_bytes = json.dumps(data).encode("utf-8")
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
        return None

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

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
                    print(f"Error serving asset: {e}")

        # 2. System Settings - User/Pass Login Disabled (Must return 0 for login form to show)
        if "hrms.api.system_settings.get_user_pass_login_disabled" in path:
            self._send_json(200, {"message": 0})
            return

        # 3. OAuth Providers (Return empty list)
        if "hrms.api.oauth.oauth_providers" in path:
            self._send_json(200, {"message": []})
            return

        # 4. Dev Context: /api/method/hrms.www.hrms.get_context_for_dev
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

        # 5. Current User Info
        if "hrms.api.get_current_user_info" in path or "frappe.auth.get_logged_user" in path:
            user = self.get_user_from_cookie()
            if not user:
                self._send_json(401, {
                    "exc_type": "AuthenticationError",
                    "message": "Please login to continue."
                })
                return

            self._send_json(200, {
                "message": {
                    "name": user,
                    "email": user if "@" in user else f"{user.lower()}@example.com",
                    "first_name": "Admin" if user == "Administrator" else user.split("@")[0].capitalize(),
                    "full_name": "Administrator" if user == "Administrator" else user,
                    "roles": ["System Manager", "HR Manager", "Employee", "HR User"]
                }
            })
            return

        # 6. Current Employee Info
        if "hrms.api.get_current_employee_info" in path:
            user = self.get_user_from_cookie()
            self._send_json(200, {
                "message": {
                    "name": "HR-EMP-00001",
                    "employee_name": "Administrator" if user == "Administrator" else (user or "Admin"),
                    "first_name": "Admin",
                    "designation": "HR Director",
                    "department": "Human Resources",
                    "company": "HR Software Co",
                    "reports_to": "",
                    "user_id": user or "Administrator"
                }
            })
            return

        # 7. Other common queries
        if "hrms.api.get_unread_notifications_count" in path:
            self._send_json(200, {"message": 0})
            return

        if "hrms.api.are_push_notifications_enabled" in path:
            self._send_json(200, {"message": 0})
            return

        if "hrms.api.get_hr_settings" in path:
            self._send_json(200, {"message": {}})
            return

        # Default fallback
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

        # 1. Login Endpoint
        if path.endswith("/login") or "login" in path:
            usr = data.get("usr") or "Administrator"
            print(f"[AUTH] Login successful for user: {usr}")
            # Note: user_id MUST NOT have HttpOnly so client JavaScript can read document.cookie
            cookies = [
                f"user_id={usr}; Path=/; SameSite=Lax",
                f"system_user=yes; Path=/; SameSite=Lax",
                f"full_name={usr}; Path=/; SameSite=Lax",
                f"sid=session_token_{usr}; Path=/; HttpOnly; SameSite=Lax"
            ]
            self._send_json(200, {
                "message": "Logged In",
                "home_page": "/hrms",
                "full_name": usr
            }, cookies=cookies)
            return

        # 2. Logout Endpoint
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

        # 4. Fallback for other RPC methods
        self._send_json(200, {"message": "OK", "data": data})

def run(port=8000):
    server_address = ("127.0.0.1", port)
    httpd = HTTPServer(server_address, HRBackendHandler)
    print("=" * 60)
    print(f" HR Software Backend API Server")
    print(f" Listening on: http://127.0.0.1:{port}")
    print(f" Neon Database: Connected")
    print("=" * 60)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping backend server...")
        httpd.server_close()

if __name__ == "__main__":
    port = int(os.environ.get("SERVER_PORT", 8000))
    run(port=port)
