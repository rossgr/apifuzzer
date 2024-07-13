import colorama
from colorama import Fore, Style
import requests
import sys
import argparse
import validators

def arg_handler():
    parser = argparse.ArgumentParser(prog="F-UWU", description="Python API Fuzzer")
    parser.add_argument('-u', '--url', required=True)
    parser.add_argument('-w', '--wordlist', required=True)
    parser.add_argument('-v', '--version') 
    parser.add_argument('-r', '--request', required=True)

    args = parser.parse_args();
    if validators.url(args.url):
        match args.request.upper():
            case "GET":
                httpGET(args.url, args.wordlist)
            case "POST":
                httpPOST(args.url, args.payload, args.wordlist)
            case _:
                exit()
    else:
        print("Invalid URL type")    


        
    

def wordListLoad(wlist):
    words = open(wlist, 'r')
    wordlist = words.readlines();
    return wordlist

def httpGET(URL, wlist):
    wordListLoad(wlist)
    for word in wordListLoad(wlist):
        res = requests.get(url=f'{URL}{word}')
        print(res)
        print(f'{URL}{word}')
        if res.status_code == 404:
            continue
        elif res.status_code <= 299 or res.status_code >=200:
            JSON_data = res.json()
            print(Fore.GREEN + word + '' + res.status_code)
            print(JSON_data)

def httpPOST(URL, PAYLOAD, wlist):
    wordListLoad(wlist)
    for word in wordListLoad(wlist):
        res = requests.get(url=f'{URL}{word}')
    
print(Fore.MAGENTA + '''  ______           __  __  __ __ __  __  __      
/_____/\         /_/\/_/\/_//_//_/\/_/\/_/\     
\::::_\/_  ______\:\ \:\ \:\\:\\:\ \:\ \:\ \    
 \:\/___/\/______/\:\ \:\ \:\\:\\:\ \:\ \:\ \   
  \:::._\/\__::::\/\:\ \:\ \:\\:\\:\ \:\ \:\ \  
   \:\ \            \:\_\:\ \:\\:\\:\ \:\_\:\ \ 
    \_\/             \_____\/\_______\/\_____\/ 
                                                
                                                ''')
    
    
arg_handler()