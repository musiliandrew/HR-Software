"""
Database migration & seeder for Neon PostgreSQL.
Creates the relational schema and populates rich sample data for HR Software.
"""

import os
from datetime import datetime, date, timedelta
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    print("Error: DATABASE_URL not found in .env")
    exit(1)

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def create_schema(cur):
    print("Creating tables in Neon PostgreSQL...")

    # Users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) UNIQUE NOT NULL,
        email VARCHAR(150) UNIQUE NOT NULL,
        first_name VARCHAR(100),
        full_name VARCHAR(150),
        roles TEXT[] DEFAULT '{"Employee"}',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Employees table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL,
        employee_name VARCHAR(150) NOT NULL,
        first_name VARCHAR(100),
        designation VARCHAR(100),
        department VARCHAR(100),
        company VARCHAR(100) DEFAULT 'HR Software Co',
        reports_to VARCHAR(50),
        user_id VARCHAR(150),
        status VARCHAR(50) DEFAULT 'Active',
        image TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Leave Types table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS leave_types (
        name VARCHAR(100) PRIMARY KEY,
        max_days_allowed INT DEFAULT 21,
        is_carry_forward BOOLEAN DEFAULT true
    );
    """)

    # Leave Allocations table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS leave_allocations (
        id SERIAL PRIMARY KEY,
        employee VARCHAR(50) REFERENCES employees(name) ON DELETE CASCADE,
        leave_type VARCHAR(100) REFERENCES leave_types(name) ON DELETE CASCADE,
        total_allocated INT DEFAULT 0,
        leaves_remaining INT DEFAULT 0,
        year INT DEFAULT 2026
    );
    """)

    # Leave Applications table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS leave_applications (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL,
        employee VARCHAR(50) REFERENCES employees(name) ON DELETE CASCADE,
        employee_name VARCHAR(150),
        leave_type VARCHAR(100),
        from_date DATE NOT NULL,
        to_date DATE NOT NULL,
        total_leave_days INT NOT NULL,
        status VARCHAR(50) DEFAULT 'Draft',
        docstatus INT DEFAULT 0,
        description TEXT,
        leave_approver VARCHAR(150),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Employee Checkins (Clock-in / Clock-out)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employee_checkins (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL,
        employee VARCHAR(50) REFERENCES employees(name) ON DELETE CASCADE,
        employee_name VARCHAR(150),
        log_type VARCHAR(10) NOT NULL,
        time TIMESTAMP NOT NULL,
        device_id VARCHAR(100) DEFAULT 'Web PWA',
        latitude NUMERIC(10, 6),
        longitude NUMERIC(10, 6)
    );
    """)

    # Shifts table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS shift_types (
        name VARCHAR(100) PRIMARY KEY,
        start_time TIME NOT NULL,
        end_time TIME NOT NULL
    );
    """)

    # Shift Requests
    cur.execute("""
    CREATE TABLE IF NOT EXISTS shift_requests (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL,
        employee VARCHAR(50) REFERENCES employees(name) ON DELETE CASCADE,
        employee_name VARCHAR(150),
        shift_type VARCHAR(100),
        from_date DATE NOT NULL,
        to_date DATE NOT NULL,
        status VARCHAR(50) DEFAULT 'Approved',
        docstatus INT DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Attendance Requests
    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance_requests (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL,
        employee VARCHAR(50) REFERENCES employees(name) ON DELETE CASCADE,
        employee_name VARCHAR(150),
        from_date DATE NOT NULL,
        to_date DATE NOT NULL,
        reason VARCHAR(100),
        status VARCHAR(50) DEFAULT 'Approved',
        docstatus INT DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Expense Claim Types
    cur.execute("""
    CREATE TABLE IF NOT EXISTS expense_claim_types (
        name VARCHAR(100) PRIMARY KEY
    );
    """)

    # Expense Claims
    cur.execute("""
    CREATE TABLE IF NOT EXISTS expense_claims (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL,
        employee VARCHAR(50) REFERENCES employees(name) ON DELETE CASCADE,
        employee_name VARCHAR(150),
        total_claimed_amount NUMERIC(12, 2) NOT NULL,
        total_sanctioned_amount NUMERIC(12, 2) NOT NULL,
        status VARCHAR(50) DEFAULT 'Approved',
        docstatus INT DEFAULT 1,
        posting_date DATE DEFAULT CURRENT_DATE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Salary Slips
    cur.execute("""
    CREATE TABLE IF NOT EXISTS salary_slips (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL,
        employee VARCHAR(50) REFERENCES employees(name) ON DELETE CASCADE,
        employee_name VARCHAR(150),
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        gross_pay NUMERIC(12, 2) NOT NULL,
        net_pay NUMERIC(12, 2) NOT NULL,
        status VARCHAR(50) DEFAULT 'Submitted'
    );
    """)

    print("Tables created successfully.")

def seed_data(cur):
    print("Seeding sample records into Neon PostgreSQL...")

    # 1. Users
    cur.execute("""
    INSERT INTO users (name, email, first_name, full_name, roles) VALUES
    ('Administrator', 'admin@example.com', 'Admin', 'Administrator', '{"System Manager", "HR Manager", "Employee", "HR User"}'),
    ('andrew@example.com', 'andrew@example.com', 'Andrew', 'Andrew Musili', '{"System Manager", "HR Manager", "Employee"}'),
    ('sarah.connor@example.com', 'sarah.connor@example.com', 'Sarah', 'Sarah Connor', '{"Employee"}'),
    ('michael.scott@example.com', 'michael.scott@example.com', 'Michael', 'Michael Scott', '{"Employee"}'),
    ('dwight.schrute@example.com', 'dwight.schrute@example.com', 'Dwight', 'Dwight Schrute', '{"Employee"}')
    ON CONFLICT (name) DO UPDATE SET roles = EXCLUDED.roles;
    """)

    # 2. Employees
    cur.execute("""
    INSERT INTO employees (name, employee_name, first_name, designation, department, company, reports_to, user_id, status) VALUES
    ('HR-EMP-00001', 'Administrator', 'Admin', 'HR Director', 'Human Resources', 'HR Software Co', '', 'Administrator', 'Active'),
    ('HR-EMP-00002', 'Andrew Musili', 'Andrew', 'Lead Software Engineer', 'Engineering', 'HR Software Co', 'HR-EMP-00001', 'andrew@example.com', 'Active'),
    ('HR-EMP-00003', 'Sarah Connor', 'Sarah', 'Operations Lead', 'Operations', 'HR Software Co', 'HR-EMP-00001', 'sarah.connor@example.com', 'Active'),
    ('HR-EMP-00004', 'Michael Scott', 'Michael', 'Regional Manager', 'Management', 'HR Software Co', 'HR-EMP-00001', 'michael.scott@example.com', 'Active'),
    ('HR-EMP-00005', 'Dwight Schrute', 'Dwight', 'Sales Executive', 'Sales', 'HR Software Co', 'HR-EMP-00004', 'dwight.schrute@example.com', 'Active')
    ON CONFLICT (name) DO UPDATE SET designation = EXCLUDED.designation;
    """)

    # 3. Leave Types
    cur.execute("""
    INSERT INTO leave_types (name, max_days_allowed) VALUES
    ('Annual Leave', 21),
    ('Casual Leave', 7),
    ('Sick Leave', 10),
    ('Maternity Leave', 90),
    ('Compensatory Off', 5)
    ON CONFLICT (name) DO NOTHING;
    """)

    # 4. Leave Allocations for Administrator
    cur.execute("""
    DELETE FROM leave_allocations WHERE employee = 'HR-EMP-00001';
    INSERT INTO leave_allocations (employee, leave_type, total_allocated, leaves_remaining, year) VALUES
    ('HR-EMP-00001', 'Annual Leave', 21, 18, 2026),
    ('HR-EMP-00001', 'Casual Leave', 7, 5, 2026),
    ('HR-EMP-00001', 'Sick Leave', 10, 10, 2026),
    ('HR-EMP-00001', 'Compensatory Off', 5, 3, 2026);
    """)

    # 5. Leave Applications
    cur.execute("""
    INSERT INTO leave_applications (name, employee, employee_name, leave_type, from_date, to_date, total_leave_days, status, docstatus, description) VALUES
    ('HR-LV-2026-00001', 'HR-EMP-00001', 'Administrator', 'Annual Leave', '2026-11-20', '2026-11-22', 3, 'Approved', 1, 'Short trip with family'),
    ('HR-LV-2026-00002', 'HR-EMP-00001', 'Administrator', 'Casual Leave', '2026-12-05', '2026-12-06', 2, 'Pending', 0, 'Personal appointments'),
    ('HR-LV-2026-00003', 'HR-EMP-00002', 'Andrew Musili', 'Annual Leave', '2026-11-25', '2026-11-28', 4, 'Approved', 1, 'End of year vacation')
    ON CONFLICT (name) DO NOTHING;
    """)

    # 6. Check-ins
    now = datetime.now()
    cur.execute("""
    INSERT INTO employee_checkins (name, employee, employee_name, log_type, time, device_id) VALUES
    ('CHECKIN-001', 'HR-EMP-00001', 'Administrator', 'IN', %s, 'Web PWA'),
    ('CHECKIN-002', 'HR-EMP-00001', 'Administrator', 'OUT', %s, 'Web PWA'),
    ('CHECKIN-003', 'HR-EMP-00002', 'Andrew Musili', 'IN', %s, 'Mobile PWA')
    ON CONFLICT (name) DO NOTHING;
    """, (
        now - timedelta(hours=4),
        now - timedelta(minutes=45),
        now - timedelta(hours=3)
    ))

    # 7. Shift Types
    cur.execute("""
    INSERT INTO shift_types (name, start_time, end_time) VALUES
    ('Morning Shift', '08:00:00', '16:00:00'),
    ('General Shift', '09:00:00', '17:00:00'),
    ('Evening Shift', '16:00:00', '00:00:00')
    ON CONFLICT (name) DO NOTHING;
    """)

    # 8. Shift Requests
    cur.execute("""
    INSERT INTO shift_requests (name, employee, employee_name, shift_type, from_date, to_date, status, docstatus) VALUES
    ('HR-SR-2026-00001', 'HR-EMP-00001', 'Administrator', 'General Shift', '2026-11-01', '2026-11-30', 'Approved', 1),
    ('HR-SR-2026-00002', 'HR-EMP-00002', 'Andrew Musili', 'Morning Shift', '2026-11-01', '2026-11-30', 'Approved', 1)
    ON CONFLICT (name) DO NOTHING;
    """)

    # 9. Attendance Requests
    cur.execute("""
    INSERT INTO attendance_requests (name, employee, employee_name, from_date, to_date, reason, status, docstatus) VALUES
    ('HR-ATT-2026-00001', 'HR-EMP-00001', 'Administrator', '2026-11-10', '2026-11-10', 'Work From Home', 'Approved', 1),
    ('HR-ATT-2026-00002', 'HR-EMP-00002', 'Andrew Musili', '2026-11-08', '2026-11-08', 'On Duty - Client Visit', 'Approved', 1)
    ON CONFLICT (name) DO NOTHING;
    """)

    # 10. Expense Claim Types
    cur.execute("""
    INSERT INTO expense_claim_types (name) VALUES
    ('Travel'),
    ('Meals & Entertainment'),
    ('Office Supplies'),
    ('Telephone & Internet'),
    ('Medical Expenses')
    ON CONFLICT (name) DO NOTHING;
    """)

    # 11. Expense Claims
    cur.execute("""
    INSERT INTO expense_claims (name, employee, employee_name, total_claimed_amount, total_sanctioned_amount, status, docstatus, posting_date) VALUES
    ('HR-EXP-2026-00001', 'HR-EMP-00001', 'Administrator', 285.50, 285.50, 'Approved', 1, '2026-11-05'),
    ('HR-EXP-2026-00002', 'HR-EMP-00002', 'Andrew Musili', 120.00, 120.00, 'Approved', 1, '2026-11-09')
    ON CONFLICT (name) DO NOTHING;
    """)

    # 12. Salary Slips
    cur.execute("""
    INSERT INTO salary_slips (name, employee, employee_name, start_date, end_date, gross_pay, net_pay, status) VALUES
    ('HR-SS-2026-10-001', 'HR-EMP-00001', 'Administrator', '2026-10-01', '2026-10-31', 6500.00, 5200.00, 'Submitted'),
    ('HR-SS-2026-09-001', 'HR-EMP-00001', 'Administrator', '2026-09-01', '2026-09-30', 6500.00, 5200.00, 'Submitted'),
    ('HR-SS-2026-10-002', 'HR-EMP-00002', 'Andrew Musili', '2026-10-01', '2026-10-31', 5800.00, 4700.00, 'Submitted')
    ON CONFLICT (name) DO NOTHING;
    """)

    print("Data seeded successfully!")

def main():
    conn = get_connection()
    conn.autocommit = True
    cur = conn.cursor()
    create_schema(cur)
    seed_data(cur)
    cur.close()
    conn.close()
    print("Database initialization complete.")

if __name__ == "__main__":
    main()
