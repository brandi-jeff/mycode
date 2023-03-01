#!/usr/bin/python3

## for accepting arguments from the cmd line
import argparse

import requests

import pandas as pd

ITEMURL = "http://pokeapi.co/api/v2/item/"
POKEURL = "https://pokeapi.co/api/v2/pokemon/"
def main():

    pokemon = requests.get(f"{POKEURL}?LIMIT=1000")
    pokemon = pokemon.json()
    #TODO need to figure out this for loop to print the pokemon name
    for name in pokemon.get("results"):
        namedf = pd.DataFrame(name)
        print(namedf)

    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    #create a list to store items with the word searched on
    matchedwords = []

    for item in items.get("results"):
        if args.searchword in item.get("name"):
            matchedwords.append(item.get("name"))

    finishedlist = matchedwords.copy()
    
    #map our matchedword list to a dict with a title
    matchedwords = {}
    matchedwords["matched"] = finishedlist

    #list all words containing matched word
    print(f"There are {len(finishedlist)} words that contain the word '{args.searchword}' in the Pokemon Item API!")
    print(f"List of Pokemon items containing '{args.searchword}': ")
    print(matchedwords)

    itemsdf = pd.DataFrame(matchedwords)
    itemsdf.to_excel("pokemonitems.xlsx", index=False)

    print("Gotta catch 'em all!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass in a word to search\
    the Pokemon item API")
    parser.add_argument('--searchword', metavar='SEARCHW',\
    type=str, default='ball', help="Pass in any word. Default is 'ball'")
    args = parser.parse_args()
    main()

