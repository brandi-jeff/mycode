#!/usr/bin/python3
"""A simple Flask server with multiple endpoints.""" 
   
# /success/<name>
   
# / or /start - Both endpoints respond with 200 + postmaker.html (template)
   
# /login          
# a POST will have the form read for 'nm'
# a GET will be scanned for the query param ?nm=some_value

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"

@app.route("/")
@app.route("/start")
def start():
   
    #looks for templates/postmaker.html
    return render_template("postmaker.html")

#This is where postmaker.html POSTs data to
#A user could also browser (GET) to this location
#methods has to equal a list
@app.route("/login", methods = ["POST", "GET"])
def login():
    #POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        #if nm was assigned via the POST and grab the value of nm from the POST
        if request.form.get("nm"): 
            user = request.form.get("nm") 
        else: 
            user = "defaultuser"
    
    #GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("nm"): # if nm was assigned as a parameter=value
            user = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
        else:
            user = "defaultuser" 
    return redirect(url_for("success", name = user)) # pass back to /success with value for name
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

