# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:37:59 2020

@author: platf
"""

#  Problem 1: IOU!

#  starter code list
disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"]


#  review contents of list for specific characters ad print statements

for index, value_at_that_index in enumerate(disney_characters):
    if 'u' in value_at_that_index:
        print(value_at_that_index + " U are so Uniquely U!")
    elif 'i' in value_at_that_index:
        print(value_at_that_index + " I bet you're Impressively Intelligent!")
    elif 'o' in value_at_that_index:
        print(value_at_that_index + " O My! How Original!")
    else:
        print(value_at_that_index  + " Ehh, a's and e's are so ordinary.")
        

#  Problem 2: If You're Cold, Sit in a Corner. It's 90 Degrees!

#  While the temperature is greater than 75 degrees Fahrenheit, print "The temperature is XX — crank the AC!" 
#  and subtract 3 degrees from the temperature.
#  Once the temperature is cool enough and the loop is done, print "75. Ahh, that's better.

temperature = 90
ideal_temp = 75

while temperature > ideal_temp:
    print("The temperature is "+ str(temperature) +" — crank the AC!")
    temperature -= 3
print(str(temperature) +". Ahh, that's better.")
    