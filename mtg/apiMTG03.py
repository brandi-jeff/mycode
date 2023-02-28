#!/usr/bin/env python3
"""interact with an "open" api,
   https://api.magicthegathering.io/v1/"""

import requests

#Define our "base" API
API = "https://api.magicthegathering.io/v1/" 

def main():
    """Run time code"""

    resp = requests.get(f"{API}sets") 

    # the .json() method will dump a JSON string into Pythonic data structures
    # This is much easier than using the urllib.request library
    print( resp.json() )

if __name__ == "__main__":
    main()

