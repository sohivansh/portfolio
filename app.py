from flask import Flask, request, redirect
from flask import render_template
import sqlite3

con = sqlite3.connect('database.db',check_same_thread=False)
cur = con.cursor() 
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def layout():
    cur.execute("SELECT likes FROM likes")
    likes = cur.fetchone()[0]
    return render_template("index.html",likes=likes)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/like",methods=["POST","GET"])
def like():
    if request.method == "POST":
        cur.execute("SELECT likes FROM likes")
        temp = cur.fetchone()
        likes = int(temp[0])
        likes += 1
        cur.execute("UPDATE likes SET likes = ?", (likes,))
        con.commit()
        return redirect("/")

