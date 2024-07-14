import colorama
from colorama import Fore, Style
import requests
import sys
import argparse
import validators
import json

def arg_handler():
    parser = argparse.ArgumentParser(prog="F-UWU", description="Python API Fuzzer")
    parser.add_argument('-u', '--url', required=True)
    parser.add_argument('-w', '--wordlist', required=True)
    parser.add_argument('-v', '--version') 
    parser.add_argument('-pt', '--textpayload')
    parser.add_argument('-pj', '--jsonpayload')
    parser.add_argument('-r', '--request', required=True)

    args = parser.parse_args();
    if validators.url(args.url):
        match args.request.upper():
            case "GET":
                httpGET(args.url, args.wordlist)
            case "POST":
                if args.textpayload:
                    httpPOST(args.url, args.textpayload, args.wordlist)
                if args.jsonpayload:
                    httpPOST(args.url, args.jsonpayload, args.wordlist)
            case _:
                exit()
    else:
        print("Invalid URL type")    


def wordListLoad(wlist):
    words = open(wlist, 'r')
    wordlist = words.readlines()
    return wordlist

def payloadListLoad(payload):
    pload = open(payload, 'r')
    payloads = pload.readlines()
    return payloads

    
def JSONListLoad(payload):
    jsonList = open(f'{payload}.json')
    data = json.load(jsonList)
    return data

def httpGET(URL, wlist):
    wordListLoad(wlist)
    for word in wordListLoad(wlist):
        res = requests.get(url=f'{URL}{word}')
        if res.status_code <= 599 or res.status_code >= 400 :
            print(Fore.RED + word + ' ' + str([res.status_code]))
        elif res.status_code <= 299 or res.status_code >=200:
            print(Fore.GREEN + word + ' ' + str([res.status_code]))

def httpPOST(URL, payload, wlist):
    for word in wordListLoad(wlist):
        for pload in payloadListLoad(payload):
            res = requests.post(url=f'{URL}{word}', data=pload)
    
print(Fore.MAGENTA + 
r'''  ______           __  __  __ __ __  __  __      
/_____/\         /_/\/_/\/_//_//_/\/_/\/_/\     
\::::_\/_  ______\:\ \:\ \:\\:\\:\ \:\ \:\ \    
 \:\/___/\/______/\:\ \:\ \:\\:\\:\ \:\ \:\ \   
  \:::._\/\__::::\/\:\ \:\ \:\\:\\:\ \:\ \:\ \  
   \:\ \            \:\_\:\ \:\\:\\:\ \:\_\:\ \ 
    \_\/             \_____\/\_______\/\_____\/ 
                                                
                                                ''' + '\n')
    
    
arg_handler()