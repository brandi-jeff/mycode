#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    ## Send HTTPS GET to the API of ICE and Fire books resource
    gotresp = requests.get(AOIF_BOOKS)

    ## Decode the response
    got_dj = gotresp.json()

    ## loop across response
    for book in got_dj:
        ## display the names of each book
        print(f"{book['name']}, pages - {book['numberOfPages']}")
        print(f"\tAPI URL -> {book['url']}\n")
        
        # print ISBN
        print(f"\tISBN -> {book['isbn']}\n")
        print(f"\tPUBLISHER -> {book['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(book['characters'])}\n")

if __name__ == "__main__":
    main()
