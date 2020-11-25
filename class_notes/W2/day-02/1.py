# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


items = [1, 2, 3]

items.append(10)   # used to add to the end of the list

print(items)


#  a tuple means once you create it -- you can not change it

name_tuple =    ("Suresh", "Melvin", "Juan", "Suresh")

#name_tuple[1] = "Melvin"  # tuple object does not support item assignment.

# use a tuple to protect the data within the list 

print(name_tuple.count("Suresh"))  # output = 2 as there are two object that are equal

print(name_tuple.index("Melvin"))  # output = 1 as the index of the object is the 1st (after 0 index)


print(name_tuple.index("Suresh"))   #  returns the index 0 as its the first one in the tuple. 
                                    #  stops searching the rest of the values
                                    

                                    
                                


