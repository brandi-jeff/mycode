#!/usr/bin/env python3

''' First simple flask server'''

from flask import Flask

#Flask constructor takes name of current module as an argument
app = Flask(__name__)

'''route() function of the Flask class is a decorator; it tells the application which URL
   should call the associated function '''
#when client reaches this end point.. run the function
@app.route("/")
def hello_world():
    return "Hello World"
app.add_url_rule("/hello", "hello", hello_world)

if __name__ == "__main__":
    #0.0.0.0 means all ip addresses
    app.run(host="0.0.0.0", port=2224)
