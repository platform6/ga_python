# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 19:16:51 2020

@author: platf
"""

x = 10


try:
    # this is where we write the code
    # where we think its going to break out program
    print(x)
except:
    # this is where we handle the error
    print("An error has occurred")

print("Hello world")



print(" \n" * 3)




a = 0
b = 10

try:
    print( b / a )
except:
    print("Can not divide by 0")


list_a =  [1, 2, 3]

print(list_a[0])

try:
    print(list_a[100])
except:
    print(list_a[-1])

