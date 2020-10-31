# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:04:31 2020

@author: platf
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:30:04 2020

@author: platf
"""

from math import pi


class Circle:



    def __init__(self, radius):
        self.__radius = radius
        self.__diameter = radius * 2
        self.__area = pi * radius ** 2

    def __set_diameter(self, diameter):
        self.__diameter = diameter
        self.__radius = diameter / 2
        self.__area = pi * self.radius ** 2

    def __set_radius(self, radius):
         self.__radius = radius
         self.__diameter = radius * 2
         self.__area = pi * radius ** 2

    def __get_diameter(self):
         return self.__diameter

    def __get_radius(self):
        return self.__radius

    def __get_area(self):
        return self.__area

    # https://realpython.com/instance-class-and-static-methods-demystified/
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    # https://www.journaldev.com/22460/python-str-repr-functions#python--str
    def __repr__(self):
        return f'Circle({self.radius})'

    def __str__(self):
        return f'Circle({self.radius})'

    def __lt__(self, other):
        return self.__radius < other.__radius

    def __add__(self, other):
        return self.__radius + other.__radius

    def __mul__(self, other):
        return float(self.__radius * other)

    def __eq__(self, other):
        return self.__radius == other.__radius

    def __gt__(self, other):
        return self.__radius > other.__radius


    diameter = property(fset=__set_diameter, fget = __get_diameter)
    radius = property(fset=__set_radius, fget=__get_radius)
    area = property(fget=__get_area)  # set as read only as it is a calculated value



# test code
# define the first circle and display its attributes
c1 = Circle(4)
print(c1.radius, c1.diameter)
print('^^^ Expected output: 4 8 \n')
print(c1.area)
print('^^^ Expected output: 50.26548245743669 \n')


# change the diameter -- the radius and area should change correspondingly
c1.diameter = 2
print(c1.radius, c1.area)
print('^^^ Expected output: 1.0 3.141592653589793 \n')


# define a circle using the from_diameter method
c2 = Circle.from_diameter(10)
print(c2.radius, c2.area)
print('^^^ Expected output: 5.0 78.53981633974483 \n')

# create two more circles; put all the circle objects inside a list named circles
c3 = Circle(6)
c4 = Circle(1.1)
circles = [c1, c2, c3, c4]
print(circles)
print('^^^ Expected output: [Circle(1.0), Circle(5.0), Circle(6), Circle(1.1)] \n')

# sort the list of circles
print(sorted(circles))
print('^^^ Expected output: [Circle(1.0), Circle(1.1), Circle(5.0), Circle(6)] \n')


# add two circles
c5 = c3 + c4
print(c5)
print('^^^ Expected output: Circle with Radius: 7.1 \n')

# multiply a circle by a number
c6 = c3 * 5
print(c6)
print('^^^ Expected output: Circle with Radius: 30.0 \n')


# see if two circles with equal radii evaluate as equal
c4.radius = 1
print(c4 == c1)
print('^^^ Expected output: True \n')


# Compare two circles to see which is bigger.

c7 = Circle(10)
c8 = Circle(12)

print(c8 > c7)
print('^^^ Expected output: True ')

c7 = Circle(12)
c8 = Circle(10)

print(c8 > c7)
print('^^^ Expected output: False ')