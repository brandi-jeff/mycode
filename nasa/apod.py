#!/usr/bin/env 

"""Making requests to NASA API with dev key"""

import pprint
import urllib.request
import json

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    #remove any "extra" new line feeds on our key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    
    #call webservice with key
    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds)

    #read file
    apodread = apodurlobj.read()

    #decode JSON to Python
    apod = json.loads(apodread.decode("utf-8"))

    #display Pythonic data
    print("\n\nConverted Python data")
    print(apod)
    print('__________________________________')

    print()

    print(f'Here is the url for the picture: {apod["url"]}.')

    print(f"The picture {apod['title']} was taken on {apod['date']}.")

    print(f'Explanation of {apod["title"]}: {apod["explanation"]}')


if __name__ == "__main__":
    main()
