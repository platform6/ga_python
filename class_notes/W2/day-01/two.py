# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:54:33 2020

@author: platf
"""

my_list = [1, 2, 3, "Joe", 11.1]

print(1 in my_list)  # prints true as that object exists in my list

name = "Garrett"

print('a' in name)  # prints true as the 'a' is part of the iterable string


#  age = 22

#  print(22 in age)  # TypeError: argument of type 'int' is not iterable

# can only iterate through a list of values - can not iterate through integers or floats, or booleans, 
# or None types



for number in my_list:   # my_list is called the iterable,  number = iterator!
    print(number)


# find the type of the iterator
for number in my_list:   
    print(type(number))
    
    
print(len(my_list))  # prints 5



for i in range(4):    #fives you 0-3 index - 4 items
    print("hello --- world")
    
for number in range(len(my_list)):
    print(number, my_list[number])    # this guarantees that the iterator will remain an integer


for number in range(len(my_list)):
    print(number, type(my_list[number]))  #the //number// iterator is used to access the list object and retrieve the value
    

print("now --- the third way")


names = ["Jordan", "Melvin", "Sharon"]

for index, value_at_that_index in enumerate(names):
    print(index, value_at_that_index)
    

for index, value_at_that_index in enumerate(names):  # looking at the hex id - it points to same hex as calling index directly.
    print(index, hex(id(value_at_that_index)))
    

print("Check to see if saem memory space as the for loop id")
print(hex(id(names[0])))
    

