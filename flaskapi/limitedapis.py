#!/usr/bin/python3
"""Using the Flask-Limiter package to set limits on individual API requests from an IP."""

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

#describes when to trigger function
@app.route("/slow")
#describes how often to trigger function
@limiter.limit("1 per day")
def slow():
    return "Enjoy this message now. You won't see it again until tomorrow."


@app.route("/fast")
def fast():
    return "I inherited the default limits of 200 per day and 50 per hour, so I don't need a limiter."

@app.route("/ping")
#removes all limits on this API
@limiter.exempt
def ping():
    return "I am immortal!!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
