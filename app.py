from flask import Flask ,render_template , session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "Oggy&Jack"

db = SQLAlchemy(app)

@app.route("/")
def login():
    return render_template("login.html")    

@app.route("/faculty")
def faculty():
    hod_name = session.get("hod_name")
    hod_email = session.get("hod_email")

    

    return render_template("hod_dashboard.html")
    
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
