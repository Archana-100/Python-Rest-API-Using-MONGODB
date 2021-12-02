# -*- coding: utf-8 -*-
"""
check all request
@author: archa
"""
import requests
import json

API_ENDPOINT = "http://127.0.0.1:9091//college_d"

raw_dict = {
            'name':"avi",
            'address':"vashi"
            }

raw_dict_update = {
            'name':"suresh",
            'update_address' : "saideep"
            }

raw_dict_delete = {
            'name':"sandepep"
            }


r = requests.get(url = API_ENDPOINT)#json.dumps(raw_dict))
print(r.text)
print("result :%s"%r)

r2 = requests.post(url = API_ENDPOINT,json =raw_dict)
print(r2.text)
print("result :%s"%r2)

r3 = requests.put(url = API_ENDPOINT,json =raw_dict_update)
print(r3.text)
print("result :%s"%r3)

r4 = requests.delete(url = API_ENDPOINT,json =raw_dict_delete)
print(r4.text)
print("result :%s"%r4)





"""r = requests.get(url = API_ENDPOINT,json =raw_dict)#json.dumps(raw_dict))
print(r.text)
print("result :%s"%r)"""