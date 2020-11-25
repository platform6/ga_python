# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:24:23 2020

@author: platf
"""

class ToyCar:

    def __init__(self):
        self.name = None
        self.color = None
        self.weight = None

    def __eq__(self, other):
        #  print(f"objectA {self} __eq__objectB {other}")
        return self.name == other.name and self.color == other.color

    def __add__ (self, other):
        #  print(f"objectA {self} __add__objectB {other}")
        return self.weight + other.weight

    def __mul__(self, other):
        return self.weight * other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __str__(self):
        return "this is a toyCar"


car_a = ToyCar()

car_b = ToyCar()


car_a.name = "toycar"
car_a.color = "red"
car_a.weight = 1



car_b.name = "toycar"
car_b.color = "red"
car_b.weight = 1.1


print(car_a == car_b)

print(car_a + car_b)

print(car_a * car_b)

print(car_a < car_b)

print(car_a > car_b)

print(car_a)  # calls - __str__