from datetime import datetime
from extensions import db

class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False) 
    DoB = db.Column(db.String(255), nullable=False)
    roll_number = db.Column(db.String(20), unique=True, nullable=True) 
    semester = db.Column(db.Integer, nullable=True)
    department = db.Column(db.String(100), nullable=True)
    sgpa = db.Column(db.Float, nullable=True)
    cgpa = db.Column(db.Float, nullable=True)
    scholarship = db.Column(db.String(50), nullable=True)  
    father_name = db.Column(db.String(50), nullable=True)
    mother_name = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(500), nullable=True)
    blood_group = db.Column(db.String(10), nullable=True)
    category = db.Column(db.String(20), nullable=True)
    abc_id = db.Column(db.String(50), nullable=True)
    achievements = db.Column(db.String(500), nullable=True)
    batch = db.Column(db.Integer, nullable=True)
    backlogs = db.Column(db.Integer, nullable=True)
    attendance_percentage = db.Column(db.Float, nullable=True)


class Faculty(db.Model):
    __tablename__ = "faculty"

    faculty_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    about = db.Column(db.String(700), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    qualifications = db.Column(db.String(300), nullable=False)
    core_specialization = db.Column(db.Text, nullable=True)
    professional_certifications = db.Column(db.Text, nullable=True)
    employment_type = db.Column(db.String(50))
    teaching_experience = db.Column(db.Float, default=0)
    industry_experience = db.Column(db.Float, default=0)
    assigned_laboratory = db.Column(db.String(100))
    mentorship_batch = db.Column(db.String(50), nullable=False)
    research = db.Column(db.String(500), nullable=False)
    interests = db.Column(db.String(100), nullable=False)
    joining_date = db.Column(db.String(20), nullable=False)
    cabin = db.Column(db.String(50))
    theory_lectures = db.Column(db.Integer, default=0)
    practical_sessions = db.Column(db.Integer, default=0)
    designation = db.Column(db.String(50), nullable=False)


class Admin(db.Model):
    __tablename__ = "admin"

    admin_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    about = db.Column(db.String(700), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    qualifications = db.Column(db.String(300), nullable=False)
    core_specialization = db.Column(db.Text, nullable=True)
    professional_certifications = db.Column(db.Text, nullable=True)
    employment_type = db.Column(db.String(50))
    teaching_experience = db.Column(db.Float, default=0)
    industry_experience = db.Column(db.Float, default=0)
    research = db.Column(db.String(500), nullable=False)
    interests = db.Column(db.String(100), nullable=False)
    joining_date = db.Column(db.String(20), nullable=False)
    cabin = db.Column(db.String(50))


class Notice(db.Model):
    __tablename__ = "notice"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False, default="General")  # Academic, Exam, Holiday, Urgent, General
    target_audience = db.Column(db.String(50), nullable=False, default="All")  # All, Students, Faculty
    attachment_url = db.Column(db.String(255), nullable=True)
    is_pinned = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_name = db.Column(db.String(100), default="Head of Department")


# Aliases for backward compatibility
student = Student
faculty = Faculty

