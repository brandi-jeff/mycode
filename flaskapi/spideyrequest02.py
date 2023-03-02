#!/usr/bin/env python3
import json
from pprint import pprint

import requests

URL= "http://127.0.0.1:2224/"

new_hero= {
           "name": "Wolverine",
           "realName": "James Howlett",
           "since": 1974,
           "powers": ["adamantium skeleton","claws","regeneration"]
          }

#json.dumps takes a python obj and returns as JSON string
new_hero = json.dumps(new_hero)

resp = requests.post(URL, json = new_hero)

#strip the json
pprint(resp.json())
