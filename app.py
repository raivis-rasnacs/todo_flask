from flask import (
    Flask,
    render_template,
    redirect,
    request
)
import sqlite3

app = Flask(__name__)

@app.route("/tasks", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        ...
    return render_template("index.html")


app.run(debug=True)