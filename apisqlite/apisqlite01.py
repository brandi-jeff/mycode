#!/usr/bin/env python3
"""Access OMDB API and incorporate into local SQLite DB"""

import json
import sqlite3
import requests

OMDBURL = "http://www.omdbapi.com/?"

def movielookup(mykey, searchstring):
    """Interactions with OMDB API
       mykey = omdb api key
       searchstring = string to search for"""
    try:
        api = f"{OMDBURL}apikey={mykey}&s={searchstring}"

        resp = requests.get(api)
        return resp.json()
    except:
        return False

def trackmeplease(datatotrack):
    conn = sqlite3.connect('mymovie.db')
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS MOVIES (TITLE TEXT PRIMARY KEY NOT NULL, YEAR INT  NOT NULL);''')

        for data in datatotrack:
            
            #the ? are examples of "bind vars"; best practice, and prevents sql injection attacks
            #never ever use f-strings or concatenate (+) to build your executions
            conn.execute("INSERT INTO MOVIES (TITLE,YEAR) VALUES (?,?)",(data.get("Title"), data.get("Year")))
            conn.commit()

        print("Database operation done")
        conn.close()
        return True
    except:
        return False

def harvestkey():
    with open("/home/student/omdb.key") as apikeyfile:
        return apikeyfile.read().rstrip("\n") 

def printlocaldb():
    pass
    #cursor = conn.execute("SELECT * from MOVIES")
    #for row in cursor:
    #    print("MOVIE = ", row[0])
    #    print("YEAR = ", row[1])


def main():

    mykey = harvestkey()

    while True:
        answer = ""
        while answer == "":
            print("""\n**** Welcome to the OMDB Movie Client and DB ****
            ** Returned data will be written into the local database **
            1) Search for All Movies Containing String
            2) Search for Movies Containing String, and by Type
            99) Exit""")

            answer = input("> ")

        if answer in ["1", "2"]:
            searchstring = input("Search all movies in the OMDB. Enter search string: ")

            if answer == "1":
                resp = movielookup(mykey, searchstring)
            elif answer == "2":
                print("\nSearch by type coming soon!\n") 
                continue                                 
            if resp:
                resp = resp.get("Search")
                print(resp)
                trackmeplease(resp)
            else:
                print("That search did not return any results.")

        elif answer == "99":
            print("See you next time!")
            break

if __name__ == "__main__":
    main()

