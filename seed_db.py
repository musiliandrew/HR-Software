"""
Database migration & multi-tenant SaaS seeder for Neon PostgreSQL.
Establishes Company (Tenant) boundaries, subscription plans, seat allocations,
and tenant-scoped employee & payroll records.
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
    print("Migrating schema to Multi-Tenant B2B SaaS architecture...")

    # 1. Tenants (Companies / Organizations)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tenants (
        id VARCHAR(50) PRIMARY KEY,
        name VARCHAR(150) NOT NULL,
        slug VARCHAR(100) UNIQUE NOT NULL,
        billing_email VARCHAR(150) NOT NULL,
        plan_tier VARCHAR(50) DEFAULT 'Growth',
        seat_limit INT DEFAULT 50,
        status VARCHAR(50) DEFAULT 'Active',
        currency VARCHAR(10) DEFAULT 'USD',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 2. Subscriptions & Billing
    cur.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        id SERIAL PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE,
        stripe_customer_id VARCHAR(100),
        stripe_subscription_id VARCHAR(100),
        plan_name VARCHAR(50) NOT NULL,
        monthly_price NUMERIC(10, 2) NOT NULL,
        billing_cycle VARCHAR(20) DEFAULT 'monthly',
        status VARCHAR(50) DEFAULT 'active',
        current_period_end TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 3. Users (with tenant linkage & RBAC)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE,
        name VARCHAR(100) UNIQUE NOT NULL,
        email VARCHAR(150) UNIQUE NOT NULL,
        first_name VARCHAR(100),
        full_name VARCHAR(150),
        role VARCHAR(50) DEFAULT 'Employee',
        roles TEXT[] DEFAULT '{"Employee"}',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    # Add tenant_id if table previously existed without it
    cur.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE;")
    cur.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS role VARCHAR(50) DEFAULT 'Employee';")

    # 4. Employees
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE,
        name VARCHAR(50) UNIQUE NOT NULL,
        employee_name VARCHAR(150) NOT NULL,
        first_name VARCHAR(100),
        designation VARCHAR(100),
        department VARCHAR(100),
        company VARCHAR(100),
        reports_to VARCHAR(50),
        user_id VARCHAR(150),
        status VARCHAR(50) DEFAULT 'Active',
        image TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    cur.execute("ALTER TABLE employees ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE;")

    # 5. Leave Types
    cur.execute("""
    CREATE TABLE IF NOT EXISTS leave_types (
        name VARCHAR(100) PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE,
        max_days_allowed INT DEFAULT 21,
        is_carry_forward BOOLEAN DEFAULT true
    );
    """)
    cur.execute("ALTER TABLE leave_types ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE;")

    # 6. Leave Allocations
    cur.execute("""
    CREATE TABLE IF NOT EXISTS leave_allocations (
        id SERIAL PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE,
        employee VARCHAR(50) REFERENCES employees(name) ON DELETE CASCADE,
        leave_type VARCHAR(100) REFERENCES leave_types(name) ON DELETE CASCADE,
        total_allocated INT DEFAULT 0,
        leaves_remaining INT DEFAULT 0,
        year INT DEFAULT 2026
    );
    """)
    cur.execute("ALTER TABLE leave_allocations ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE;")

    # 7. Leave Applications
    cur.execute("""
    CREATE TABLE IF NOT EXISTS leave_applications (
        id SERIAL PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE,
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
    cur.execute("ALTER TABLE leave_applications ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE;")

    # 8. Employee Checkins
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employee_checkins (
        id SERIAL PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE,
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
    cur.execute("ALTER TABLE employee_checkins ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE;")

    # 9. Shifts
    cur.execute("""
    CREATE TABLE IF NOT EXISTS shift_types (
        name VARCHAR(100) PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE,
        start_time TIME NOT NULL,
        end_time TIME NOT NULL
    );
    """)
    cur.execute("ALTER TABLE shift_types ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE;")

    # 10. Shift Requests
    cur.execute("""
    CREATE TABLE IF NOT EXISTS shift_requests (
        id SERIAL PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE,
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
    cur.execute("ALTER TABLE shift_requests ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE;")

    # 11. Attendance Requests
    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance_requests (
        id SERIAL PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE,
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
    cur.execute("ALTER TABLE attendance_requests ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE;")

    # 12. Expense Claim Types
    cur.execute("""
    CREATE TABLE IF NOT EXISTS expense_claim_types (
        name VARCHAR(100) PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE
    );
    """)
    cur.execute("ALTER TABLE expense_claim_types ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE;")

    # 13. Expense Claims
    cur.execute("""
    CREATE TABLE IF NOT EXISTS expense_claims (
        id SERIAL PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE,
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
    cur.execute("ALTER TABLE expense_claims ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE;")

    # 14. Salary Slips
    cur.execute("""
    CREATE TABLE IF NOT EXISTS salary_slips (
        id SERIAL PRIMARY KEY,
        tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE,
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
    cur.execute("ALTER TABLE salary_slips ADD COLUMN IF NOT EXISTS tenant_id VARCHAR(50) REFERENCES tenants(id) ON DELETE CASCADE;")

    print("Multi-tenant tables and constraints successfully verified.")

def seed_data(cur):
    print("Seeding multi-tenant companies & subscription plans...")

    # 1. Tenants (Companies)
    cur.execute("""
    INSERT INTO tenants (id, name, slug, billing_email, plan_tier, seat_limit, status) VALUES
    ('TENANT-ACME', 'Acme Corporation', 'acme', 'billing@acme.com', 'Growth', 50, 'Active'),
    ('TENANT-GLOBEX', 'Globex Industries', 'globex', 'finance@globex.com', 'Starter', 15, 'Active')
    ON CONFLICT (id) DO UPDATE SET 
        name = EXCLUDED.name,
        plan_tier = EXCLUDED.plan_tier,
        seat_limit = EXCLUDED.seat_limit;
    """)

    # 2. Subscriptions
    cur.execute("""
    DELETE FROM subscriptions WHERE tenant_id IN ('TENANT-ACME', 'TENANT-GLOBEX');
    INSERT INTO subscriptions (tenant_id, stripe_customer_id, stripe_subscription_id, plan_name, monthly_price, billing_cycle, status, current_period_end) VALUES
    ('TENANT-ACME', 'cus_acme_live123', 'sub_acme_growth99', 'Growth Plan (50 Seats)', 79.00, 'monthly', 'active', CURRENT_TIMESTAMP + INTERVAL '25 days'),
    ('TENANT-GLOBEX', 'cus_globex_live456', 'sub_globex_starter11', 'Starter Plan (15 Seats)', 29.00, 'monthly', 'active', CURRENT_TIMESTAMP + INTERVAL '18 days');
    """)

    # 3. Users for Acme Corp
    cur.execute("""
    INSERT INTO users (name, tenant_id, email, first_name, full_name, role, roles) VALUES
    ('Administrator', 'TENANT-ACME', 'admin@example.com', 'Admin', 'HR Lead (Acme)', 'Company Owner', '{"Company Owner", "System Manager", "HR Manager", "Employee"}'),
    ('andrew@example.com', 'TENANT-ACME', 'andrew@example.com', 'Andrew', 'Andrew Musili', 'HR Admin', '{"HR Manager", "Employee"}'),
    ('sarah.connor@example.com', 'TENANT-ACME', 'sarah.connor@example.com', 'Sarah', 'Sarah Connor', 'Employee', '{"Employee"}'),
    ('michael.scott@example.com', 'TENANT-ACME', 'michael.scott@example.com', 'Michael', 'Michael Scott', 'Employee', '{"Employee"}'),
    ('dwight.schrute@example.com', 'TENANT-ACME', 'dwight.schrute@example.com', 'Dwight', 'Dwight Schrute', 'Employee', '{"Employee"}')
    ON CONFLICT (name) DO UPDATE SET 
        tenant_id = EXCLUDED.tenant_id,
        role = EXCLUDED.role,
        roles = EXCLUDED.roles;
    """)

    # 4. Employees for Acme Corp
    cur.execute("""
    INSERT INTO employees (name, tenant_id, employee_name, first_name, designation, department, company, reports_to, user_id, status) VALUES
    ('HR-EMP-00001', 'TENANT-ACME', 'Administrator', 'Admin', 'HR Director & VP', 'Human Resources', 'Acme Corporation', '', 'Administrator', 'Active'),
    ('HR-EMP-00002', 'TENANT-ACME', 'Andrew Musili', 'Andrew', 'Lead Software Engineer', 'Engineering', 'Acme Corporation', 'HR-EMP-00001', 'andrew@example.com', 'Active'),
    ('HR-EMP-00003', 'TENANT-ACME', 'Sarah Connor', 'Sarah', 'Operations Lead', 'Operations', 'Acme Corporation', 'HR-EMP-00001', 'sarah.connor@example.com', 'Active'),
    ('HR-EMP-00004', 'TENANT-ACME', 'Michael Scott', 'Michael', 'Regional Manager', 'Management', 'Acme Corporation', 'HR-EMP-00001', 'michael.scott@example.com', 'Active'),
    ('HR-EMP-00005', 'TENANT-ACME', 'Dwight Schrute', 'Dwight', 'Sales Executive', 'Sales', 'Acme Corporation', 'HR-EMP-00004', 'dwight.schrute@example.com', 'Active')
    ON CONFLICT (name) DO UPDATE SET 
        tenant_id = EXCLUDED.tenant_id,
        company = EXCLUDED.company;
    """)

    # Link existing records to Acme Corporation
    cur.execute("UPDATE leave_types SET tenant_id = 'TENANT-ACME' WHERE tenant_id IS NULL;")
    cur.execute("UPDATE leave_allocations SET tenant_id = 'TENANT-ACME' WHERE tenant_id IS NULL;")
    cur.execute("UPDATE leave_applications SET tenant_id = 'TENANT-ACME' WHERE tenant_id IS NULL;")
    cur.execute("UPDATE employee_checkins SET tenant_id = 'TENANT-ACME' WHERE tenant_id IS NULL;")
    cur.execute("UPDATE shift_types SET tenant_id = 'TENANT-ACME' WHERE tenant_id IS NULL;")
    cur.execute("UPDATE shift_requests SET tenant_id = 'TENANT-ACME' WHERE tenant_id IS NULL;")
    cur.execute("UPDATE attendance_requests SET tenant_id = 'TENANT-ACME' WHERE tenant_id IS NULL;")
    cur.execute("UPDATE expense_claim_types SET tenant_id = 'TENANT-ACME' WHERE tenant_id IS NULL;")
    cur.execute("UPDATE expense_claims SET tenant_id = 'TENANT-ACME' WHERE tenant_id IS NULL;")
    cur.execute("UPDATE salary_slips SET tenant_id = 'TENANT-ACME' WHERE tenant_id IS NULL;")

    print("Multi-tenant seeding completed successfully!")

def main():
    conn = get_connection()
    conn.autocommit = True
    cur = conn.cursor()
    create_schema(cur)
    seed_data(cur)
    cur.close()
    conn.close()
    print("Multi-tenant database initialization finished.")

if __name__ == "__main__":
    main()
