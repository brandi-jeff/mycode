#!/usr/bin/env python3
"""interact with an "open" api,
   https://api.magicthegathering.io/v1/"""

import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    """Run time code"""

    resp = requests.get(f"{API}sets")

    cardsets = resp.json().get("sets")
    
    #open a file we write our data into
    with open("mtgsets.index", "w") as mtgfile:
        for cardset in cardsets: 
            print(f"{cardset.get('name')} -- {cardset.get('code')}", file=mtgfile)

if __name__ == "__main__":
    main()
