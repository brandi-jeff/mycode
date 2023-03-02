#!/usr/bin/env python
'''creating Flas API with jinja2 templating involving some logic'''

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello! Welcome!"

#specifiy the data type using colon; default is string
@app.route("/scoretest/<int:score>")
def hello_name(score):
    return render_template("highscore.html", marks = score)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
