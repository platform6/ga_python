# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:03:08 2020

@author: platf
"""

class HR:

    def __init__(self):
        self.__name = None
        self.__age = None
        self.__address = None

    def __set_name(self, name):
        self.__name = name

    def __get_name(self):
        return self.__name

    def __set_age(self, age):
        self.__age = age


    def __get_age(self):
        return self.__age

    def __get_address(self):
        return self.__address

    def __set_address(self, address):
        self.__address = address

    address = property(fset= __set_address, fget= __get_address)
    name = property(fset= __set_name, fget= __get_name)
    age = property(fset= __set_age, fget= __get_age)


    # control read / write ability through the property attribute


employee_john = HR()

employee_john.name = "John"

print(employee_john.name)

employee_john.age  = 12

print(employee_john.age)


employee_john.address = "113 Main St"

print(employee_john.address)






