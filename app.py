from flask import Flask, session, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def login():
    return "<p>this is login page!</p>"
    

@app.route("/faculty")
def faculty():
    # HOD details are read from the session when they are available.
    hod_name = session.get("hod_name")
    hod_email = session.get("hod_email")

    # These values need a database/model, so no placeholder data is created.
    total_students = None
    total_faculty = None
    attendance_summary = None
    notices = []
    events = []

    # The existing project folder is named "tenplates".
    app.template_folder = "tenplates"

    return render_template(
        "index.html",
        hod_name=hod_name,
        hod_email=hod_email,
        total_students=total_students,
        total_faculty=total_faculty,
        attendance_summary=attendance_summary,
        notices=notices,
        events=events,
    )
    
    
if __name__ == "__main__":
    app.run(debug=True)
