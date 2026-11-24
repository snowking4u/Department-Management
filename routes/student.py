from flask import Blueprint, render_template, session, redirect, url_for, abort
from extensions import db
from models import Student

student_bp = Blueprint("student", __name__, url_prefix="/student-portal")


@student_bp.route("/dashboard")
def dashboard():
    """Student dashboard."""
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("user_role", "").lower() != "student":
        abort(403)

    current_student = Student.query.get(session["user_id"])

    # Placeholder view until student portal UI is created
    student_name = current_student.name if current_student else "Student"
    roll_no = current_student.roll_number if current_student else "N/A"
    dept = current_student.department if current_student else "N/A"

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Student Portal | GPH</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }}
            .card {{ background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); max-width: 500px; width: 100%; text-align: center; }}
            h1 {{ color: #0d47a1; margin-bottom: 10px; }}
            p {{ color: #555; font-size: 16px; line-height: 1.6; }}
            .badge {{ display: inline-block; background: #e3f2fd; color: #0d47a1; padding: 6px 14px; border-radius: 20px; font-weight: 600; margin: 10px 0; }}
            .btn {{ display: inline-block; margin-top: 20px; padding: 10px 24px; background: #0d47a1; color: white; text-decoration: none; border-radius: 6px; font-weight: 500; }}
            .btn:hover {{ background: #1565c0; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Student Portal</h1>
            <div class="badge">Computer Engineering Department</div>
            <p>Welcome, <strong>{student_name}</strong>!</p>
            <p>Roll Number: <strong>{roll_no}</strong> | Department: <strong>{dept}</strong></p>
            <p style="color: #888; font-size: 14px; margin-top: 15px;">Student portal features (Attendance, Timetable, Results, Notices) are currently under development.</p>
            <a href="{url_for('auth.logout')}" class="btn">Logout</a>
        </div>
    </body>
    </html>
    """


# ============================================================================
# NOTE: Student-specific coding is pending.
# Add your routes below whenever you are ready:
# e.g.:
# @student_bp.route("/my-attendance")
# @student_bp.route("/results")
# @student_bp.route("/profile")
# ============================================================================

