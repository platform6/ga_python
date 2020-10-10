# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:03:15 2020

@author: platf
"""

print(abs(-5))

x = abs(-200)  #  abs is a value returning function

print(x)


def square(x):  #  this is a value returning function
    y = x * x
    return y

 

def test():  #  does not allow anything beyond the return statement
    return 1
    print("hello")
    
print(test())  #  this still prints the return value of 1


#  can return any data type in python as the return - multiple data types
#  such as tuples, dictionary, list





    
    
    