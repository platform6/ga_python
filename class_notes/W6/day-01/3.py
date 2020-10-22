# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:45:32 2020

@author: platf
"""

import requests

url = "https://www.amazon.com/?ref_=nav_custrec_signin&"

response = requests.get(url)
data = response.text

print(data)