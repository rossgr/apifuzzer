# Requires an API wordlist, for ethical use only. 

import requests
import sys

TARGET_URL = ""


for word in sys.stdin:
    res = requests.get(url=f'{TARGET_URL}/{word}');
    if res.status_code == 404:
        continue
    else:
        print(JSON_data)

