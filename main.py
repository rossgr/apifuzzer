import requests
import sys

response = requests.get(url=f'http://10.10.11.1.161/api');
print(response)
