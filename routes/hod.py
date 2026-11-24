from flask import Blueprint, render_template, session, redirect, url_for, abort
from extensions import db
from models import Student, Faculty, Admin

hod_bp = Blueprint("hod", __name__)


def require_hod():
    """Helper to verify HOD session"""
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    if session.get("user_role", "").lower() != "hod":
        abort(403)
    return None


@hod_bp.route("/hod_dashboard")
def hod_dashboard():
    redirect_resp = require_hod()
    if redirect_resp:
        return redirect_resp

    # Fetch logged-in HOD
    hod = Admin.query.get(session["user_id"])
    if not hod:
        session.clear()
        return redirect(url_for("auth.login"))

    # Dynamic counts for summary cards
    total_students = Student.query.count()
    total_faculty = Faculty.query.count()
    low_attendance_count = Student.query.filter(
        Student.attendance_percentage < 75
    ).count()

    return render_template(
        "hod_dashboard.html",
        hod=hod,
        total_students=total_students,
        total_faculty=total_faculty,
        low_attendance_count=low_attendance_count
    )


@hod_bp.route("/student-management")
def student_management():
    redirect_resp = require_hod()
    if redirect_resp:
        return redirect_resp

    students = Student.query.all()
    return render_template("student_management.html", students=students)


@hod_bp.route("/faculty")
def faculty_management():
    redirect_resp = require_hod()
    if redirect_resp:
        return redirect_resp

    faculty_users = Faculty.query.all()

    faculty_users_data = [
        {
            "id": user.faculty_id,
            "name": user.name,
            "email": user.email,
            "designation": user.designation,
            "qualifications": user.qualifications,
        }
        for user in faculty_users
    ]

    return render_template(
        "faculty.html",
        faculty_users=faculty_users,
        faculty_users_data=faculty_users_data
    )

