#!/usr/bin/env python3

import requests

API = "https://pokeapi.co/api/v2/pokemon/"

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get(API + pokenum).json()
    print(pokeapi)

    print(f"{pokeapi['name']} image- {pokeapi['sprites']['front_default']}")
    imgurl= pokeapi['sprites']['front_default']


if __name__ == "__main__":
    main()

