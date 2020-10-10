# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 18:09:17 2020

@author: platf
"""

class Student: 
    
    def __init__(self):
        #  this is an instance variable
        #  and all objects will have their own
        #  copy
        self.name = None
        
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def __str__(self):
        return "This is a student"
    

#  driver code -- or the execution point
def main():
    #intstantiated a variable assigning the Student() object to it
    mike = Student()
    mike.set_name("Mike")
    print(mike.get_name())
    print(hex(id(mike)))  # prints the memory address
    print(mike)  #  prints the memory address as well
                 #  adding the __str__ will print the return value for that class


if __name__ == '__main__':
    main()