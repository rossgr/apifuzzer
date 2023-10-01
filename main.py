# To run:
# $ cat YOURWORDLIST.txt | python main.py 

import colorama
from colorama import Fore, Style
import requests
import sys

# TODO Include optional menu for users to select type of request etc.

def menuScreen():
    TARGET_URL = input( Fore.WHITE + "Enter target URL")
    # TODO Check valid URL with ping. 
    userChoice = input('''1. GET \n 2. POST \n 3. PUT \n 4. DELETE \n 5. PATCH \n 6. HEAD ''')
    if userChoice == '1':
        httpGET(TARGET_URL)
    else:
        return "err"
    
def httpGET(TARGET_URL):
    for word in sys.stdin:
        print(TARGET_URL);
        res = requests.get(url=f'{TARGET_URL}{word}');
        if res.status_code == 404:
            print( Fore.RED + word + '' + res.status_code)
        elif res.status_code <= 299 or res.status_code >=200:
            JSON_data = res.json()
            print(Fore.GREEN + word + '' + res.status_code)
            print(JSON_data)
    


   
print(Fore.MAGENTA + '''  ______           __  __  __ __ __  __  __      
/_____/\         /_/\/_/\/_//_//_/\/_/\/_/\     
\::::_\/_  ______\:\ \:\ \:\\:\\:\ \:\ \:\ \    
 \:\/___/\/______/\:\ \:\ \:\\:\\:\ \:\ \:\ \   
  \:::._\/\__::::\/\:\ \:\ \:\\:\\:\ \:\ \:\ \  
   \:\ \            \:\_\:\ \:\\:\\:\ \:\_\:\ \ 
    \_\/             \_____\/\_______\/\_____\/ 
                                                
                                                ''')
    
    
menuScreen()


# TODO Add validator for URLs, ensure no blank URL or script will not inform user till end of wordlist.

# TODO Increase functionality beyond returning active endpoints such as changing request type. 
