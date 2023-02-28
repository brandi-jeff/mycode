#!/usr/bin/python3
"""opening a static file containing JSON data"""

import json

def main():
    """runtime code"""
    with open("datacenter.json", "r") as datacenter:
        datacenterdecoded = json.load(datacenter)

    ## This is now a dictionary
    print(type(datacenterdecoded))

    print(datacenterdecoded)

    print(datacenterdecoded["row3"])

    print(datacenterdecoded["row2"][1])

if __name__ == "__main__":
    main()

