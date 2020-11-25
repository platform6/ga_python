# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:45:06 2020

@author: platf
"""

#  two dictionary objects
dict1 = {
    "first_name" : "John", 
    "last_name" : "Doe", 
    "classes_taken" : ('Python', 'Java'),
    "grades" : (100, 55)
 }

dict2 = {
    "first_name" : "Suresh", 
    "last_name" : "Sigera", 
    "classes_taken" : ('Python', 'Java', 'C++'),
    "grades" : (100, 78)
 }


#  dictionary within a dictionay
#  the integer is the key, and the value is equal to th
#  associated dictionary value
data = {
        1: {
            "first_name" : "John", 
            "last_name" : "Doe", 
            "classes_taken" : ('Python', 'Java'),
            "grades" : (100, 55)
        },
         
        2: {
            "first_name" : "Suresh", 
            "last_name" : "Sigera", 
            "classes_taken" : ('Python', 'Java', 'C++'),
            "grades" : (100, 78)
        }
            
}


for key, value in data.items():
    # print(key, value)  #  prints integers and dictionary objects
    for i, j in value.items():
        print( i, j)
    

