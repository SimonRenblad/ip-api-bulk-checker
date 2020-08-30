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

def LookupBatch(data):
    try:
        response = requests.request('POST','http://ip-api.com/batch?fields=66846719',data=json.dumps(data)).json()
        time.sleep(5)
    except:
        print("exceeded throttle limit")
    return response

