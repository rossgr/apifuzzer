# To run:
# $ Add wordlist of your choice to same directory as file. Change words to name of wordlist

import colorama
from colorama import Fore, Style
import requests
import sys

# TODO Include optional menu for users to select type of request etc.

def menuScreen():
    TARGET_URL = input( Fore.WHITE + "Enter target URL: \n")
    # TODO Check valid URL 
    userChoice = input('''1. GET \n 2. POST \n 3. PUT \n 4. DELETE \n 5. PATCH \n 6. HEAD \n ''')
    if userChoice == '1':
        httpGET(TARGET_URL)
    else:
        return "err"
    
def httpGET(TARGET_URL):
    words = open('small.txt', 'r')
    wordlist = words.readlines()
    for word in wordlist:
        print(TARGET_URL);
        res = requests.get(url=f'{TARGET_URL}{word}');
        if res.status_code == 404:
            continue
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
