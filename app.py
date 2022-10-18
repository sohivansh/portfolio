from flask import Flask
from flask import render_template

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def layout():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

