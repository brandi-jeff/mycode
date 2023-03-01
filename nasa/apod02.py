#!/usr/bin/env python3

"""Make requests to NASA API"""

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def returncreds():
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    nasacreds = 'api_key=' +  nasacreds.strip("\n")
    return nasacreds

def main():
    nasacreds = returncreds()

    apod = requests.get(NASAAPI + nasacreds).json()

    print(apod)
    print()

if __name__ == "__main__":
    main()
