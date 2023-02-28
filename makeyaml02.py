#!/usr/bin/env python3

'''return a YAML string.. yaml.dumps() expects single argument'''

import yaml

def main():
    """runtime code"""
    
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    yamlstring = yaml.dump(hitchhikers)

    print(yamlstring)

if __name__ == "__main__":
    main()
