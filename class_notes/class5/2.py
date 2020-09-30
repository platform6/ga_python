# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:35:53 2020

@author: platf
"""

x = 10   # x is the object and 10 is the value





class House: 
    
    
    
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    # this is a method as its within the class
    def set_owner(self, owner_name):
        print("The owner name is " + owner_name)
        


#  my_house is an object of the type of House()
#  my_house = House()

# creating an object with the required arugments

a_big_house = House('Jim', 'Johnson')

# within that object calling the set_owner method
a_big_house.set_owner("Gary")


print("The person in a big house is " + a_big_house.first_name)





#  checking type = House()
#  print(type(my_house))
#  <class '__main__.House'>

#  my_house.set_owner("Suresh")


#  your_house = House()

#  your_house.set_owner("Garrett")


#  print(dir(my_house))
#  print(dir(your_house))


#  The dir() function returns all properties and methods of the specified object,
#  without the values. This function will return all the properties and methods, even 
#  built-in properties which are default for all object. that's why we see 'set_owner' in
#  both objects





    