from flask import Flask, render_template, session, request , redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
import os
import re

app = Flask(__name__)

if os.environ.get("VERCEL") != "1":
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SECRET_KEY"] = "Oggy&Jack"

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
    hod_name = session.get("hod_name")
    hod_email = session.get("hod_email")

        # Get data from login form
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")
    role = request.form.get("role", "")

        # Find user in database
    user = User.query.filter_by(email=email).first()

        # Verify password and selected role
    if (
        user
        and check_password_hash(user.password_hash, password)
        and user.role.lower() == role.lower()
    ):

    # Create login session
        session["user_id"] = user.id
        session["user_name"] = user.name
        session["user_role"] = user.role

    return render_template(
            "login.html",
            error="Invalid email, password, or selected role."
        )



@app.route("/hod-dashboard")
def hod_dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if session.get("user_role", "").lower() != "hod":
        return "Access denied", 403

    return render_template("hod_dashboard.html")

    




@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return "Registration backend is ready. Submit registration data with a POST request."

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    submitted_role = request.form.get("role", "").strip().lower()
    role = "hod" if submitted_role in {"hod", "admin"} else submitted_role
    department = request.form.get("department", "").strip()
    roll_number = request.form.get("roll_number", "").strip()
    semester = request.form.get("semester", "").strip()

    if role not in {"student", "faculty", "hod"}:
        return "Please select a valid account type.", 400
    if not name or not email or not password or not department:
        return "Name, email, password, and department are required.", 400
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return "Please enter a valid email address.", 400
    if role == "student" and (not roll_number or not semester):
        return "Student registration requires roll number and semester.", 400
    if User.query.filter_by(email=email).first():
        return "An account with this email already exists.", 400
    if role == "student" and User.query.filter_by(roll_number=roll_number).first():
        return "An account with this roll number already exists.", 400
    if role == "hod":
        configured_key = os.environ.get("HOD_REGISTRATION_KEY")
        submitted_key = request.form.get("hod_access_key", "")

        if not configured_key:
            return "Admin/HOD registration is not configured yet. Please contact the system administrator.", 403
        if submitted_key != configured_key:
            return "A valid Admin/HOD access key is required.", 403

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
    return "Account registered successfully.", 201

    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)

