#!/usr/bin/python3
""" Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        got_char = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        gotresp = requests.get(AOIF_CHAR + got_char)

        got_dj = gotresp.json()
        pprint.pprint(got_dj)

if __name__ == "__main__":
        main()

