import os
import re
from flask import Blueprint, render_template, session, request, redirect, url_for, abort
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import Student, Faculty, Admin

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        role = request.form.get("role", "").strip().lower()

        # Student Login: Roll Number + DOB
        if role == "student":
            roll_number = request.form.get("roll_number", "").strip()
            dob = request.form.get("dob", "").strip()

            user = Student.query.filter_by(roll_number=roll_number).first()

            if user and user.DoB == dob:
                session["user_id"] = user.id
                session["user_name"] = user.name
                session["user_role"] = "student"
                return redirect(url_for("student.dashboard"))

        # Faculty Login: Email + Password
        elif role == "faculty":
            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")

            user = Faculty.query.filter(
                db.func.lower(Faculty.email) == email
            ).first()

            if user and check_password_hash(user.password_hash, password):
                session["user_id"] = user.faculty_id
                session["user_name"] = user.name
                session["user_role"] = "faculty"
                session["user_email"] = user.email
                return redirect(url_for("faculty.dashboard"))

        # Admin / HOD Login: Email + Password
        elif role == "hod":
            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")

            user = Admin.query.filter(
                db.func.lower(Admin.email) == email
            ).first()

            if user and check_password_hash(user.password_hash, password):
                session["user_id"] = user.admin_id
                session["user_name"] = user.name
                session["user_role"] = "hod"
                session["user_email"] = user.email
                return redirect(url_for("hod.hod_dashboard"))

        return render_template(
            "login.html", error="Invalid credentials or selected role."
        )

    # Already logged-in user check
    if "user_id" in session:
        user_role = session.get("user_role", "").lower()

        if user_role == "hod":
            return redirect(url_for("hod.hod_dashboard"))
        elif user_role == "faculty":
            return redirect(url_for("faculty.dashboard"))
        elif user_role == "student":
            return redirect(url_for("student.dashboard"))

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    # Only Admin (HOD) is allowed to register accounts
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("user_role", "").lower() != "hod":
        abort(403)

    requested_role = request.args.get("role", "student").strip().lower()
    selected_role = "hod" if requested_role == "admin" else requested_role

    if selected_role not in {"student", "faculty", "hod"}:
        selected_role = "student"

    if request.method == "GET":
        return render_template(
            "registration.html",
            selected_role=selected_role
        )

    # Helper functions for numeric fields
    def optional_float(field_name, default=None):
        value = request.form.get(field_name, "").strip()
        if not value:
            return default
        return float(value)

    def optional_int(field_name, default=None):
        value = request.form.get(field_name, "").strip()
        if not value:
            return default
        return int(value)

    def form_error(message, status=400):
        return render_template(
            "registration.html",
            selected_role=role,
            error=message
        ), status

    # Common fields
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()

    submitted_role = request.form.get("role", "").strip().lower()
    role = "hod" if submitted_role in {"hod", "admin"} else submitted_role

    if role not in {"student", "faculty", "hod"}:
        role = selected_role

    if role not in {"student", "faculty", "hod"}:
        return form_error("Invalid account type.")

    if not name or not email:
        return form_error("Name and email are required.")

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return form_error("Please enter a valid email address.")

    # Check duplicate email in all three tables
    email_exists = (
        Student.query.filter(db.func.lower(Student.email) == email).first()
        or Faculty.query.filter(db.func.lower(Faculty.email) == email).first()
        or Admin.query.filter(db.func.lower(Admin.email) == email).first()
    )

    if email_exists:
        return form_error("This email is already registered.")

    try:
        # =========================
        # STUDENT REGISTRATION
        # =========================
        if role == "student":
            roll_number = request.form.get("roll_number", "").strip()

            if roll_number and Student.query.filter_by(
                roll_number=roll_number
            ).first():
                return form_error("This roll number is already registered.")

            mobile_number = request.form.get("mobile_number", "").strip()
            dob = request.form.get("dob", "").strip()

            if not mobile_number or not dob:
                return form_error("Mobile number and DOB are required.")

            user = Student(
                name=name,
                email=email,
                mobile_number=mobile_number,
                DoB=dob,
                roll_number=roll_number or None,
                semester=optional_int("semester"),
                department=request.form.get("department", "").strip() or None,
                sgpa=optional_float("sgpa"),
                cgpa=optional_float("cgpa"),
                scholarship=request.form.get("scholarship", "").strip() or None,
                father_name=request.form.get("father_name", "").strip() or None,
                mother_name=request.form.get("mother_name", "").strip() or None,
                address=request.form.get("address", "").strip() or None,
                blood_group=request.form.get("blood_group", "").strip() or None,
                category=request.form.get("category", "").strip() or None,
                abc_id=request.form.get("abc_id", "").strip() or None,
                achievements=request.form.get("achievements", "").strip() or None,
                batch=optional_int("batch"),
                backlogs=optional_int("backlogs"),
                attendance_percentage=optional_float("attendance_percentage")
            )

        # =========================
        # FACULTY REGISTRATION
        # =========================
        elif role == "faculty":
            password = request.form.get("password", "")
            phone_number = request.form.get("phone_number", "").strip()
            qualifications = request.form.get("qualifications", "").strip()
            about = request.form.get("about", "").strip()
            mentorship_batch = request.form.get("mentorship_batch", "").strip()
            research = request.form.get("research", "").strip()
            interests = request.form.get("interests", "").strip()
            joining_date = request.form.get("joining_date", "").strip()
            designation = request.form.get("designation", "").strip()

            if not all([
                password, phone_number, qualifications, about,
                mentorship_batch, research, interests,
                joining_date, designation
            ]):
                return form_error("Please fill all required faculty fields.")

            user = Faculty(
                name=name,
                email=email,
                password_hash=generate_password_hash(password),
                about=about,
                phone_number=phone_number,
                qualifications=qualifications,
                mentorship_batch=mentorship_batch,
                research=research,
                interests=interests,
                joining_date=joining_date,
                designation=designation,
                core_specialization=request.form.get("core_specialization", "").strip() or None,
                professional_certifications=request.form.get("professional_certifications", "").strip() or None,
                employment_type=request.form.get("employment_type", "").strip() or None,
                teaching_experience=optional_float("teaching_experience", 0),
                industry_experience=optional_float("industry_experience", 0),
                assigned_laboratory=request.form.get("assigned_laboratory", "").strip() or None,
                cabin=request.form.get("cabin", "").strip() or None,
                theory_lectures=optional_int("theory_lectures", 0),
                practical_sessions=optional_int("practical_sessions", 0)
            )

        # =========================
        # HOD / ADMIN REGISTRATION
        # =========================
        else:
            password = request.form.get("password", "")
            phone_number = request.form.get("phone_number", "").strip()
            qualifications = request.form.get("qualifications", "").strip()
            about = request.form.get("about", "").strip()
            research = request.form.get("research", "").strip()
            interests = request.form.get("interests", "").strip()
            joining_date = request.form.get("joining_date", "").strip()

            if not all([
                password, phone_number, qualifications,
                about, research, interests, joining_date
            ]):
                return form_error("Please fill all required HOD fields.")

            configured_key = os.environ.get("HOD_REGISTRATION_KEY", "admin123")
            submitted_key = request.form.get("hod_access_key", "")

            if not submitted_key or submitted_key != configured_key:
                return form_error("Invalid HOD registration access key.", 403)

            user = Admin(
                name=name,
                email=email,
                password_hash=generate_password_hash(password),
                about=about,
                phone_number=phone_number,
                qualifications=qualifications,
                research=research,
                interests=interests,
                joining_date=joining_date,
                core_specialization=request.form.get("core_specialization", "").strip() or None,
                professional_certifications=request.form.get("professional_certifications", "").strip() or None,
                employment_type=request.form.get("employment_type", "").strip() or None,
                teaching_experience=optional_float("teaching_experience", 0),
                industry_experience=optional_float("industry_experience", 0),
                cabin=request.form.get("cabin", "").strip() or None
            )

        db.session.add(user)
        db.session.commit()

        return render_template(
            "registration.html",
            selected_role=role,
            success=f"{role.title()} account registered successfully!"
        )

    except ValueError:
        db.session.rollback()
        return form_error("Please enter valid numeric values in numeric fields.")

    except Exception:
        db.session.rollback()
        return form_error("Registration failed. Please try again.")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

