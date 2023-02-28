#!/usr/bin/env python3

'''Reviewing oh to parse JSON'''

import json

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)


    with open("galaxyguide.json", "w") as zfile:
        json.dump(hitchhikers, zfile)


if __name__ == "__main__":
    main()
