import requests
import json
import time

def Lookup(ip):
    try:
        data = requests.get("http://ip-api.com/json/{}?fields=66846719".format(ip)).json()
        time.sleep(2)
    except:
        data = {'status':'fail'}
    return data # Defaults to None if failed to get block value
