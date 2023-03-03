#!/usr/bin/python3
"""A simple Flask server to upload and download files"""

from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/uploader", methods = ["POST", "GET"])
def upload_file():
    if request.method == "GET":
         return render_template("upload.html")

    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))
        return "You successfully uploade a file."

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
