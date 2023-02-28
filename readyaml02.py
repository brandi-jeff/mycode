#!/usr/bin/python3
"""yaml.load() expects a single file and
   converts the YAML to pythonic data"""

import yaml

def main():
    """runtime code"""
    with open("myYAML.yml", "r") as myf:
        pyyammy = yaml.load(myf, Loader=yaml.FullLoader)
    print(pyyammy)

    pyyammy[0]['apps'].append('minecraft')
    print(pyyammy)
    
    with open("myYAML.yml.updated", "w") as myf:
        yaml.dump(pyyammy, myf)


if __name__ == "__main__":
    main()
