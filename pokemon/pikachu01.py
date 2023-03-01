#!/usr/bin/python3

import requests

POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    #Make HTTP GET request using requests, and decode
    #Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    #JSON attachment as pythonic data structure
    pokemon = pokemon.json()

    #Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        print(poke.get("name"))

    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")

if __name__ == "__main__":
    main()

