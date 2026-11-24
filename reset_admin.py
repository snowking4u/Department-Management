"""
Temporary script to reset Admin data in the database.
Deletes existing admins and creates a fresh HOD account:
Email: admin@gmail.com
Password: admin1234
"""

from app import app
from extensions import db
from models import Admin
from werkzeug.security import generate_password_hash

def reset_admin():
    with app.app_context():
        # 1. Purge all existing admins
        deleted_count = Admin.query.delete()
        db.session.commit()
        print(f"Deleted {deleted_count} old admin account(s).")

        # 2. Create fresh HOD / Admin account
        fresh_admin = Admin(
            name="Head of Department",
            email="admin@gmail.com",
            password_hash=generate_password_hash("admin1234"),
            about="Head of Computer Engineering Department, overseeing academic operations, faculty coordination, and student development.",
            phone_number="+91 9876543210",
            qualifications="Ph.D. in Computer Science & Engineering, M.Tech (CSE)",
            core_specialization="Artificial Intelligence, Distributed Systems & Database Architecture",
            professional_certifications="Certified Cloud Architect, IEEE Senior Member",
            employment_type="Permanent / Full-Time",
            teaching_experience=15.0,
            industry_experience=4.0,
            research="Artificial Intelligence, High Performance Computing, Scalable Database Systems",
            interests="Data Structures, Deep Learning, Higher Education Leadership",
            joining_date="2016-07-15",
            cabin="Cabin 101, Ground Floor, Department Block"
        )

        db.session.add(fresh_admin)
        db.session.commit()

        print("==========================================")
        print("Fresh Admin account created successfully!")
        print("Role:     HOD")
        print("Name:     Head of Department")
        print("Email:    admin@gmail.com")
        print("Password: admin1234")
        print("==========================================")

if __name__ == "__main__":
    reset_admin()

