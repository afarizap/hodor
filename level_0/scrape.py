#!/usr/bin/env python3

import requests

URL = 'http://158.69.76.135/level0.php'
myobj = {'id': '1633', 'holdthedoor': 'Submit'}
i = 0
for i in range(10):
    x = requests.post(URL, data=myobj)
