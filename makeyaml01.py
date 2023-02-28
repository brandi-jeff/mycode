#!/usr/bin/python3
"""Manipulate YAML"""

import yaml

def main():
    """runtime code"""
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    with open("galaxyguide.yaml", "w") as zfile:

        '''unlike JSON, the YAML lib uses .dump() to create YAML strings and write to files the 
        JSON lib uses .dump() to create a string and .dumps() to write to files'''
        yaml.dump(hitchhikers, zfile)

if __name__ == "__main__":
    main()

