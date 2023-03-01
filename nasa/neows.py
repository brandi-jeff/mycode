#!/usr/bin/env python3

import requests

NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def returncreds():
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

def main():
    nasacreds = returncreds()


    startdate = input("Please enter a start date (YYYY-MM-DD): ")
    enddate = input("Would you like to enter an end date? (Y/n) ")
    if enddate == "y":
       enddate = input("Please enter an end date (YYYY-MM-DD): ")

    neowrequest = requests.get(NEOURL + startdate + enddate + "&" + nasacreds)
    neowdata = neowrequest.json()

    print(neowdata)


if __name__ == "__main__":
    main()
