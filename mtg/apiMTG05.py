#!/usr/bin/env python3
"""interact with an "open" api,
   https://api.magicthegathering.io/v1/"""

import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    """Run time code"""

    resp = requests.get(f"{API}sets")

    cardsets = resp.json().get("sets")

    #loop across all of the sets of MTG cards... stored as dict objects
    for cardset in cardsets:
        print(cardset)

if __name__ == "__main__":
    main()
