import math

#  Sine and cosine
#  Write a program that reads a value representing an angle (in radians), and prints the difference between its sine and cosine.

# Do not round the result.
angle = float(input())

sine = math.sin(angle)
cosin = math.cos(angle)

print(sine - cosin)
