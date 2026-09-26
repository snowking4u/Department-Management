from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def login():
    return "<p>this is login page!</p>"
    

@app.route("/faculty")
def faculty():
    return "<p>this is  faculty dashboard page.</p>"
@app.route("/hod-dashboard")
def hod_dashboard():
    return render_template("hod_dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)