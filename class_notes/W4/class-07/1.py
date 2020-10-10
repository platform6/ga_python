# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:03:08 2020

@author: platf
"""

class HR:

    def __init__(self):
        self.name = None  # this is a public instance variable called name!

        # a private cannot be accessed outside of the class
        self.__age = None

        self.__address = None

    #  this is a public method
    #  all the objects will have access to this method

    def set_name(self, name):
        self.name = name

    #  this is a public method
    #  all the objects will have access to this method

    def get_name(self):
        return self.name


    #  public method that has access to a private instance variable
    def set_age(self, age):
        self.__age = age

    #  public method that has access to a private instance variable
    def get_age(self):
        return self.__age

    #  adding __ to the mehod name turns it into a private instance method
    def __get_address(self):
        return self.__address

    #  adding __ to the mehod name turns it into a private instance method
    def __set_address(self, address):
        self.__address = address

    address = property(fset = __set_address, fget = __get_address)








employee_john = HR()

employee_john.set_name("John")
print(employee_john.get_name())

employee_john.set_age(12)

print(employee_john.get_age())


#employee_john.set_address('112 Main St')

#print(employee_john.get_address())

employee_john.address = "113 Main St"

print(employee_john.address)






