#!/usr/bin/python3
"""Acess astros on ISS API"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    groundctrl = urllib.request.urlopen(MAJORTOM)

    #strip off the attachment (JSON) and read it, the problem is that it will read out as a string
    helmet = groundctrl.read()

    #at this point, our data is str we want to convert this to list / dict
    print(helmet)

    helmetson = json.loads(helmet.decode("utf-8"))

    #bytes
    print(type(helmet))

    #dict
    print(type(helmetson))

    print(helmetson["number"])

    print(helmetson["people"])

    print(helmetson["people"][0])

    print(helmetson["people"][1])

    print(helmetson["people"][-1])

    for astro in helmetson["people"]:
        print(astro)

    for astro in helmetson["people"]:
        print(astro["name"])

if __name__ == "__main__":
    main()

