from flask import Blueprint, render_template, session, redirect, url_for, abort
from extensions import db
from models import Faculty

faculty_bp = Blueprint("faculty", __name__, url_prefix="/faculty-portal")


@faculty_bp.route("/dashboard")
def dashboard():
    """Faculty member's own dashboard / profile view."""
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("user_role", "").lower() != "faculty":
        abort(403)

    current_faculty = Faculty.query.get(session["user_id"])
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
        faculty_users_data=faculty_users_data,
        current_faculty=current_faculty
    )


# ============================================================================
# NOTE: Faculty-specific coding is pending.
# Add your routes below whenever you are ready:
# e.g.:
# @faculty_bp.route("/mark-attendance")
# @faculty_bp.route("/upload-marks")
# @faculty_bp.route("/my-classes")
# ============================================================================

