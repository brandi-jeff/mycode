#!/usr/bin/python3
"""yaml.load() expects a single file and
   converts the YAML to pythonic data"""

import yaml

def main():
    """runtime code"""
    with open("myYAML.yml", "r") as yf:
        ## convert YAML into Python data structures (lists and dictionaries)
        pyyammy = yaml.load(yf, Loader=yaml.FullLoader)
    print(pyyammy)

if __name__ == "__main__":
    main()

