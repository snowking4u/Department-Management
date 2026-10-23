import os
import re
from flask import Flask, render_template, session, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "Oggy&Jack")

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    roll_number = db.Column(db.String(50), unique=True, nullable=True)
    semester = db.Column(db.String(20), nullable=True)
    department = db.Column(db.String(100), nullable=True)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        role = request.form.get("role", "").strip()

        # Find user in database
        user = User.query.filter(db.func.lower(User.email) == email).first()

        # Verify password and selected role
        if (
            user
            and check_password_hash(user.password_hash, password)
            and user.role.lower() == role.lower()
        ):
            session["user_id"] = user.id
            session["user_name"] = user.name
            session["user_role"] = user.role
            session["user_email"] = user.email

            if user.role.lower() == "hod":
                return redirect(url_for("hod_dashboard"))
            elif user.role.lower() == "faculty":
                return redirect(url_for("faculty"))
            else:
                return redirect(url_for("student_management"))

        return render_template(
            "login.html",
            error="Invalid email, password, or selected role."
        )

    # If already logged in, redirect to respective dashboard
    if "user_id" in session:
        user_role = session.get("user_role", "").lower()
        if user_role == "hod":
            return redirect(url_for("hod_dashboard"))
        elif user_role == "faculty":
            return redirect(url_for("faculty"))
        elif user_role == "student":
            return redirect(url_for("student_management"))

    return render_template("login.html")


@app.route("/hod_dashboard")
def hod_dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if session.get("user_role", "").lower() != "hod":
        return "Access denied: HOD role required.", 403

    return render_template("hod_dashboard.html")


@app.route("/student-management")
def student_management():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("student_management.html")


@app.route("/faculty")
def faculty():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return "<p>this is  faculty dashboard page.</p>"


@app.route("/register", methods=["GET", "POST"])
def register():
    requested_role = request.args.get("role", "student").strip().lower()
    role = "hod" if requested_role == "admin" else requested_role

    if role not in {"student", "faculty", "hod"}:
        role = "student"

    if request.method == "GET":
        return render_template("registration.html", selected_role=role)

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    submitted_role = request.form.get("role", "").strip().lower()
    role = "hod" if submitted_role in {"hod", "admin"} else submitted_role
    department = request.form.get("department", "").strip()
    roll_number = request.form.get("roll_number", "").strip()
    semester = request.form.get("semester", "").strip()

    if role not in {"student", "faculty", "hod"}:
        return render_template("registration.html", selected_role="student", error="Please select a valid account type."), 400
    if not name or not email or not password or not department:
        return render_template("registration.html", selected_role=role, error="Name, email, password, and department are required."), 400
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return render_template("registration.html", selected_role=role, error="Please enter a valid email address."), 400
    if role == "student" and (not roll_number or not semester):
        return render_template("registration.html", selected_role=role, error="Student registration requires roll number and semester."), 400
    if User.query.filter_by(email=email).first():
        return render_template("registration.html", selected_role=role, error="An account with this email already exists."), 400
    if role == "student" and User.query.filter_by(roll_number=roll_number).first():
        return render_template("registration.html", selected_role=role, error="An account with this roll number already exists."), 400
    if role == "hod":
        configured_key = os.environ.get("HOD_REGISTRATION_KEY", "admin123")
        submitted_key = request.form.get("hod_access_key", "")

        if not submitted_key or submitted_key != configured_key:
            return render_template("registration.html", selected_role=role, error="A valid Admin/HOD access key is required."), 403

    user = User(
        name=name,
        email=email,
        password_hash=generate_password_hash(password),
        role=role,
        roll_number=roll_number if role == "student" else None,
        semester=semester if role == "student" else None,
        department=department
    )
    db.session.add(user)
    db.session.commit()
    return render_template("registration.html", selected_role=role, success=f"{role.title()} account registered successfully!", users=user)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
