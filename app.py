import os
from flask import Flask
from extensions import db
from models import Student, Faculty, Admin

# Import blueprints
from routes.auth import auth_bp
from routes.hod import hod_bp
from routes.faculty import faculty_bp
from routes.student import student_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "Oggy&Jack")

# Initialize database
db.init_app(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(hod_bp)
app.register_blueprint(faculty_bp)
app.register_blueprint(student_bp)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
