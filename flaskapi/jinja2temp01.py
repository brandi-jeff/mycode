#!/usr/bin/env python3
'''Flask server to practice jinja2 templates'''

from flask import Flask, render_template

app = Flask(__name__)

#decorator
@app.route("/")
def index():
    return render_template("hellobasic.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

