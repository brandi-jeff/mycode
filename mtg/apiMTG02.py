#!/usr/bin/env python3
"""interact with an "open" api,
   https://api.magicthegathering.io/v1/"""

import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    """Run time code"""

    #this "f" string reads: API + "sets" OR, https://api.magicthegathering.io/v1/sets
    resp = requests.get(f"{API}sets") 

    #display the methods available to our new object
    print( dir(resp) )

if __name__ == "__main__":
    main()

