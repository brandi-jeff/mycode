#!/usr/bin/python3
"""Creating a more complex Flask server with various endpoints"""

##Endpoints
# /admin
# /guest/<guesty>
# /user/<name>

from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello, Admin"

@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"Hello, {guesty}!"

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        #if user is admin, redirect to the url for hello_admin
        #url_for take a parameter of the function as a string
        return redirect(url_for("hello_admin"))
    else:
        #goes through user path, so need to redefine guesty since that was not the original route
        return redirect(url_for("hello_guest", guesty = name))
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
