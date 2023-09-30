# Requires an API wordlist, for ethical use only. 
import colorama
from colorama import Fore, Style
import requests
import sys

TARGET_URL = ""


for word in sys.stdin:
    res = requests.get(url=f'{TARGET_URL}/{word}');
    if res.status_code == 404:
        print(Fore.RED + word)
        continue
    elif res.status_code <= 299 or res.status_code >=200:
        JSON_data = res.json()
        print(Fore.GREEN + word + '' + res.status_code)
        print(JSON_data)


