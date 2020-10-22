# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:02:33 2020

@author: platf
"""

class Student:

    # this is a class variable
    course_name = "Python 915"


    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    @classmethod
    def class_hello(cls):
    # cls = stands for class
    # self = instance
        print(f"this is a class method {cls}")

    def instance_method(self):
        print(f"this is an instance method {self}")






john = Student()
john.set_name("John")
print(john.get_name())
print(dir(john))

print(john.course_name)


john_jr = Student()
john_jr.set_name("John Jr")
print(john_jr.get_name())
print(dir(john_jr))


print(john_jr.course_name)



Student.course_name = "Full time python"


print(john_jr.course_name)


print(john.class_hello())
print(john.instance_method())
