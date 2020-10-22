# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:45:32 2020

@author: platf
"""

import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
response_data = response.json()

# print(response_data)


for person in response_data['people']:
    print(person['name'])


