#!/usr/bin/env python3

"""opening a static file containing JSON data"""

import json

def main():
    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()

    print(datacenterstring)
    print(type(datacenterstring))
    print("\nThe code above is string data. Python cannot easily work with this data.")
    input("Press Enter to continue\n")

    datacenterdecoded = json.loads(datacenterstring)

    print(type(datacenterdecoded))

    print(datacenterdecoded)

    print(datacenterdecoded["row3"])

    print(datacenterdecoded["row2"][1])

    ## write code to display the last server in row3
    print(datacenterdecoded["row3"][-1])



if __name__ == "__main__":
    main()
