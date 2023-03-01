#!/usr/bin/env python3
'''Playing with Marevl API Python Client'''

import argparse #has variable args that hold our variable  
import time       
#create our md5 hash to pass to dev.marvel.com
import hashlib    
from pprint import pprint

#3rd party
import requests

API = 'http://gateway.marvel.com/v1/public/characters'

#function to create md5 hash
def hashbuilder(rand, privkey, pubkey):
    return hashlib.md5((f"{rand}{privkey}{pubkey}").encode('utf-8')).hexdigest()


#function to call Marvel character API
def callmarvchar(rand, keyhash, pubkey, lookmeup):
    r = requests.get(f"{API}?name={lookmeup}&ts={rand}&apikey={pubkey}&hash={keyhash}")
    #check for 200 response
    if r.status_code != 200:
        response = None
    else:
        response = r.json()

    return response


def main():
    with open(args.dev) as pkey:
        privkey = pkey.read().rstrip("\n")
    
    with open(args.pub) as pkey:
        pubkey = pkey.read().rstrip('\n')

    #create an integer from a float timestamp (for our RAND)
    rand = str(time.time()).rstrip('.')

    keyhash = hashbuilder(rand, privkey, pubkey)

    result = callmarvchar(rand, keyhash, pubkey, "Wolverine")
    print(result)


if __name__ == '__main__':
    #container for argument specifications and has options that apply the parser as whole
    parser= argparse.ArgumentParser()

    #pass pub and priv keys
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')

    args = parser.parse_args()
    main()
