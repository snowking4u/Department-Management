from flask import Flask ,render_template,session,request,redirect, url_for
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os

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
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        # Get data from login form
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        role = request.form.get("role", "")

        # Find user in database
        user = User.query.filter_by(email=email).first()

        # Verify password and selected role
        if (
            user
            and check_password_hash(user.password, password)
            and user.role.lower() == role.lower()
        ):

            # Create login session
            session["user_id"] = user.id
            session["user_name"] = user.name
            session["user_role"] = user.role

        return redirect(url_for("hod_dashboard"))

    return render_template(
            "login.html",
            error="Invalid email, password, or selected role."
        )

    return render_template("login.html")



@app.route("/hod-dashboard")
def hod_dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if session.get("user_role", "").lower() != "hod":
        return "Access denied", 403

    return render_template("hod_dashboard.html")

    
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
