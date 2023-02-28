#!/usr/bin/env python3

"""json.dumps() creates a JSON string"""

import json

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]
    print(hitchhikers)

    jsonstring =json.dumps(hitchhikers)
    print(jsonstring)



if __name__ == "__main__":
    main()
