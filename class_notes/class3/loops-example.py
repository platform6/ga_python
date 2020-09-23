# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

list1 = [1, 2, 3, 4]

print(1 in list1)  # true as it is in list

print (20 in list1)  # false as the number 20 is not in the list


# loops in python 
start = 0
end = 15
for number in range(start, end):    # goes from 0 to 14 (last number not included)
    print(number)
    

print('Range with step')

start = 10
end = 25
step = 5

for x in range(start, end, step):   # range then adding step of 5 print every x5 number
    print(x)

for x in range(0, 5):       # it gets you the string 5 times 0,1,2,3,4
    print("Hello world")


    

    



