#!/usr/bin/env python3
""" interact with an "open" api,
   https://api.magicthegathering.io/v1/"""


import requests

def main():

    #request object
    resp = requests.get("https://api.magicthegathering.io/v1/sets")

    #display the methods available to our new object
    print( dir(resp) )

if __name__ == "__main__":
    main()

