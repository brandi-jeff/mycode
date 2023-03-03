#!/usr/bin/python3
"""Tracking student inventory within a sqliteDB accessed via Flask APIs"""

# standard library
import sqlite3 as sql

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec',methods = ['POST'])
def addrec():
    try:
        nm = request.form['nm']         # student name
        addr = request.form['addr']     # student street address
        city = request.form['city']     # student city
        pin = request.form['pin']       # "pin" assigned to student
                                        # ("pin" is just an example of meta data we want to track)

        with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            con.commit()
        msg = "Record successfully added"
        
    except:
        con.rollback()  # this is the opposite of a commit()
        msg = "error in insert operation"    # we were NOT successful

    finally:
        con.close()     # successful or not, close the connection to sqliteDB
        return render_template("result.html",msg = msg)    #

@app.route('/list')
def list_students():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("SELECT * from students")       
    
    rows = cur.fetchall()
    return render_template("list.html",rows = rows) 

if __name__ == '__main__':
    try:
        con = sql.connect('database.db')
        print("Opened database successfully")
        con.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
        print("Table created successfully")
        con.close()
        app.run(host="0.0.0.0", port=2224, debug = True)
    except:
        print("App failed on boot")

