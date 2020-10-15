# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:50:25 2020

@author: platf
"""



class Robot:

    def __init__(self, name, model_number, creator):
        self.name = name
        self.model_number = model_number
        self.creator = creator

    def walk(self):
        return "I'm walking using my wheels!"

    def charge(self):
        return "I'm charging ... "

class Dog:

    def __init__(self, height, weight, species=None):
        self.species = species
        self.height = height
        self.weight = weight


    def eat(self):
        return "I'm eating"

    def walk(self):
        return "I'm walking"

    def sleep(self):
        return "I'm sleeping"


class RoboDog(Robot, Dog):

    def __init__ (self, name, model_number, creator, height, weight):
        Robot.__init__(self, name, model_number, creator)
        Dog.__init__(self, height, weight)


robo_dog = RoboDog("RoboDog", 1000, "RoboLabs", 10, 200)

print(robo_dog.walk())   # can execute Robot method
print(robo_dog.eat())    # can execute Dog method


