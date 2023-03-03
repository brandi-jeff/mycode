#!/usr/bin/python3
"""Working with Flask sessions"""

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import escape
from flask import request

app = Flask(__name__)
app.secret_key = "any random string"

## If the user hits the root of our API
@app.route("/")
def index():
  if "username" in session:
    username = session["username"]
    return "Logged in as " + username + "<br>" + \
      "<b><a href = '/logout'>click here to log out</a></b>"

  return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

@app.route("/login", methods = ["GET", "POST"])
def login():
   if request.method == "POST":

      #use indexing if you know the key exists --> request.form["xyzkey"]
      #use get if the key might not exist --> request.form.get("xyzkey")
      session["username"] = request.form.get("username")
      return redirect(url_for("index"))

   #would normally put in separate html file
   return """
   <form action = "" method = "POST">
      <p><input type = text name = username></p>
      <p><input type = text name = age></p>
      <p><input type = submit value = Login></p>
   </form>
  """
@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST":
        name = request.form.get("username")
        age = request.form.get("age")

        resp = #need to make separate html file to do challenge



@app.route("/logout")
def logout():
   #.pop removes
   session.pop("username", None)
   return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=2224)

