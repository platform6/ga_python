# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:12:31 2020

@author: platf
"""

# student_name = "Suresh"
# classes_taken = ('Python', 'C', 'C++', 'Java')   #  tuple as signified by open paren
# grades = (100, 40, 41, 87)


#  curly bracket indicates dictionary type 

student_suresh = {
    'name' : 'Suresh',
    'classes_taken' : ('Python', 'C', 'C++', 'Java'),
    'grades' : (100, 40, 41, 87),
    "is_student" : True  
}

# print (type(student_suresh))   #  <class 'dict'>


#  print (student_suresh)   # prints contents keys and values

# print(student_suresh.keys())   # prints all the keys

# print(student_suresh.values())  # prints all the values


for key, value in student_suresh.items():
    print(key, value)


student_suresh["address"] = "122 Main St"   # this adds a key and the associated value

for key, value in student_suresh.items():
    print(key, value)


print('---')


student_suresh["is_student"]  = False  # this replaces the value of the existing key!! 
                                        #  can not have duplicated keys

print(student_suresh)


# a tuple can not be changed, whereas a list can
# dictonary can not have duplicate keys, each must be unique


