import math


#  The area of a circle
#  Write a program that reads an integer that represents the radius
#  of a given circle and calculates its area.
#  To calculate the area of a circle, use the following formula: S=πr2.
#  Print the result rounded to 2 decimal places.

radius = int(input())

area = math.pi * pow(radius, 2)

print(round(area, 2))
