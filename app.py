from flask import Flask

app = Flask(__name__)


@app.route("/")
def login():
    return "<p>this is login page!</p>"
    

@app.route("/faculty")
def faculty():
    return "<p>this is  faculty dashboard page.</p>"

if __name__ == "__main__":
    app.run(debug=True)