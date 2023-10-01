# To run:
# $ cat YOURWORDLIST.txt | python main.py 

import colorama
from colorama import Fore, Style
import requests
import sys

TARGET_URL = ""
def menuScreen():
    print('''  ______           __  __  __ __ __  __  __      
/_____/\         /_/\/_/\/_//_//_/\/_/\/_/\     
\::::_\/_  ______\:\ \:\ \:\\:\\:\ \:\ \:\ \    
 \:\/___/\/______/\:\ \:\ \:\\:\\:\ \:\ \:\ \   
  \:::._\/\__::::\/\:\ \:\ \:\\:\\:\ \:\ \:\ \  
   \:\ \            \:\_\:\ \:\\:\\:\ \:\_\:\ \ 
    \_\/             \_____\/\_______\/\_____\/ 
                                                
                                                
Starting script - - -''')
    
menuScreen()

for word in sys.stdin:
    res = requests.get(url=f'{TARGET_URL}/{word}');
    if res.status_code == 404:
        continue
    elif res.status_code <= 299 or res.status_code >=200:
        JSON_data = res.json()
        print(Fore.GREEN + word + '' + res.status_code)
        print(JSON_data)


