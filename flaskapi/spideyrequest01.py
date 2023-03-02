#!/usr/bin/env python3
"""making requests to our Flask API"""

from pprint import pprint

import requests 

URL = "http://127.0.0.1:2224/"

resp = requests.get(URL).json()

pprint(resp)
