# To run:
# $ Add wordlist of your choice to same directory as file. Change words to name of wordlist

import colorama
from colorama import Fore, Style
import requests
import sys
import argparse

# TODO Include optional menu for users to select type of request etc.

def handler():
    parser = argparse.ArgumentParser(prog="F-UWU", description="Python API Fuzzer")
    parser.add_argument('-u', '--url', required=True)
    parser.add_argument('-w', '--wordlist', required=True)
    parser.add_argument('-v', '--verbose')
    parser.add_argument('-z', '--version') 

    args = parser.parse_args();
    
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
    
def printHelp():
    print(Fore.BLUE + '''
        usage: python main.py -w example.txt -u https://example.org
    ''')
   
print(Fore.MAGENTA + '''  ______           __  __  __ __ __  __  __      
/_____/\         /_/\/_/\/_//_//_/\/_/\/_/\     
\::::_\/_  ______\:\ \:\ \:\\:\\:\ \:\ \:\ \    
 \:\/___/\/______/\:\ \:\ \:\\:\\:\ \:\ \:\ \   
  \:::._\/\__::::\/\:\ \:\ \:\\:\\:\ \:\ \:\ \  
   \:\ \            \:\_\:\ \:\\:\\:\ \:\_\:\ \ 
    \_\/             \_____\/\_______\/\_____\/ 
                                                
                                                ''')
    
    
handler()


# TODO Add validator for URLs, ensure no blank URL or script will not inform user till end of wordlist.

# TODO Increase functionality beyond returning active endpoints such as changing request type. 
