#!/usr/bin/env
'''Trivia question using Flask API'''
#lab 100 was my guide
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for

app = Flask(__name__)
correct = int(7)

@app.route("/")
def index():
    return render_template("trivia.html")

@app.route("/correct")
def correct():
    return render_template("answer.html")

@app.route("/answer", methods = ["POST"])
def answer():
    if request.form.get("ans") == "7":
        return redirect(url_for("correct"))
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
