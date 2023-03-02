#!/usr/bin/env python3
"""Flask application that explores using cookies."""

# endpoints
# /
# /login        - both endpoints return 200 + login.html (template)
   
# /setcookie    - POST returns 200 + cookie
#               - GET returns 302 redirect to /login
                 
# /getcookie    - reads value of userID from client cookie, then returns 200 + '<h1>Welcome {name}</h1>'
#                 where {name} is userID"""

from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/login")
@app.route("/")
def index():
    return render_template("login.html")

@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST":
        if request.form.get("nm"): 
            user = request.form.get("nm") 
        else: 
            user = "defaultuser"

        resp = make_response(render_template("readcookie.html"))
                        #cookievar #value
        resp.set_cookie("userID", user)

        return resp
        
    if request.method == "GET":
        return redirect(url_for("index")) 

@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")
    return f'<h1>Welcome {name}</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

