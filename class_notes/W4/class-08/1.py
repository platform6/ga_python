# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:26:29 2020

@author: platf
"""

class Pet:

    def __init__(self, name, species):
        print("this is a dog")
        self.name = name
        self.species = species
        self.__age = 0

    def set_species(self):
        pass

    def __talk(self):
        print('talk')


class Dog(Pet):

    def __init__(self, name):
        super().__init__(name, "Dog")







class Cat:
    pass


