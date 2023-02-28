#!/usr/bin/env python3
"""interact with an "open" api,
   https://api.magicthegathering.io/v1/"""

import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    """Run time code"""

    resp = requests.get(f"{API}sets")

    print( resp.json().keys() )

if __name__ == "__main__":
    main()

