from flask import Flask
from flask import render_template

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def layout():
    return render_template("layout.html")

@app.route("/about")
def about():
    return render_template("about.html")