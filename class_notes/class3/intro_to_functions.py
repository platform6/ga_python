# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:37:59 2020

@author: platf
"""


#def say_hello():
    #pass    #means don't do anything
    

print("this part is outside the function! ")
def say_hello():
    """
    this will print "Hello world"
    """
    print("Hello world")
    


say_hello()  
say_hello()   #runs x2 !



def add():  
    """
    this funcation will add two numbers. and print the total.

    """
    x = 100;
    y = 200;
    print(x+y)
    
add()  #  provides 300 as output


def add_version2(x, y):
    print(x + y)

add_version2(2, 4)
    