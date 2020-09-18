#!/usr/bin/env python
# coding: utf-8

# In[2]:


name = "Garrett"
age = 40
height = 6.1


# 

# In[3]:


names = ["tim", "tony","gabba","smith","mike"]


# In[4]:


names[0]


# In[5]:


type(name)


# In[6]:


type(names)


# In[7]:


grades = [] # like an empty bag - that con contain all types of different items (objects)


# In[9]:


even_numbers = [2, 4, 6, 8, 10]


# In[10]:


even_numbers


# In[11]:


even_numbers += [12, 14, 16, 18, 20]     # even_numbers is equal to 'even_numbers = even_numbers +''


# In[12]:


even_numbers


# In[13]:


prime =  [2, 3, 5, 7, 11]


# In[14]:


prime


# In[15]:


prime.pop()  # removes the last item in the list data structure


# In[16]:


prime


# In[17]:


prime.pop()


# In[18]:


prime


# In[19]:


prime.pop(0)  # removes the data at the list index = 0


# In[20]:


prime


# In[21]:


prime.clear()  #  emptys the list object of all contents


# In[22]:


prime


# In[23]:


bag = [1, 5.1, "Garrett", True]  # the list object can consist of many data types


# In[24]:


bag.pop()


# In[25]:


bag


# In[26]:


#  deleting elements from a list based on value! 
even_numbers = [2,4,6,8,10]


# In[27]:


even_numbers


# In[28]:


even_numbers.remove(8)


# In[29]:


even_numbers


# In[30]:


even_numbers += 8


# In[31]:


even_numbers += [8, 8, 8, 8, 8]


# In[32]:


even_numbers


# In[33]:


even_numbers.remove(8)  #  ends up removing just the first eight


# In[34]:


even_numbers


# In[35]:


names = ["John", "Mike"]


# In[36]:


names[0]


# In[37]:


names[1]


# In[38]:


names[1] = "Garrett"


# In[39]:


names


# In[40]:


names = ["Jim", "Mike", "Suresh"]


# In[41]:


names


# In[42]:


names.insert(1, "Sharon")  # first parameter = index,  second param = inserted item


# In[43]:


names


# In[44]:


# sorting values
a = [1, 5.3, 321, 0 ,1,2]


# In[45]:


print(a.sort())


# In[46]:


x = a.sort()


# In[47]:


print(x)


# In[48]:


a.sort()


# In[49]:


print(a)  # this prints the a list


# In[50]:


a.sort(reverse = True)  # reverses the sort


# In[51]:


print(a)


# In[52]:


first_name = "Garrett"  # variable is nothing but a placeholder that can contain any type of data
# when you request the first_name the computer doesn't know the meaning of the variable -- only the memory address


# In[53]:


id(first_name) # provides a large number - address in integer format where the firs_name variable is stored


# In[54]:


hex(id(first_name))  # provides the actual hexidecimal address of the variable


# In[55]:


first_name = "Conn"


# In[56]:


hex(id(first_name))   # created a new container for the variable with the new value


# In[57]:


first_name = "Garrett"


# In[58]:


hex(id(first_name))  # because the variable was already stored it repointed back to original version of the data


# In[59]:


del first_name  # deletes the object permanently from memory


# In[60]:


first_name


# In[61]:


last_name = ''


# In[62]:


last_name = 'Conn'


# In[63]:


last_name = None   # none means full of emptieness


# In[64]:


hex(id(last_name))


# In[65]:


age = None  


# In[66]:


hex(id(age))    # pointing at the same memory location as the none type assigned to last_namei


# In[67]:


is_pass  = True


# In[68]:


is_pass


# In[69]:


type(is_pass)  #boolean type means it can hold either true or false


# In[70]:


is_failed = False


# In[71]:


is_failed


# In[72]:


if (is_pass):               #control flow based on boolean value
    print("You passed")


# In[73]:


number = 23


# In[74]:


guess = int(input("Please enter an integer: "))


# In[75]:


number = 23
guess = int(input("Please enter an integer: "))
if guess == number:
    print("You've got it!")
else:
    print("It's wrong")        


# In[76]:


number = 23
guess = int(input("Please enter an integer: "))
if guess == number:
    print("You've got it!")
else:
    print("It's wrong")       


# In[77]:


number = 23
guess = int(input("Please enter an integer: "))
if guess == number:
    print("You've got it!")
else:
    print("It's wrong")       
print("Outside the if -- else scope")


# In[79]:


number = 42
guess = int(input("Enter an int:  "))

if guess == number:
    print("You got it")
elif guess < number:
    print("NOpe - higher ^")
elif guess > number:
    print(" Noper --- lower \/")
print("Done")
        


# In[80]:


4 != 5  #  this means not equal  - compiles into true statement


# In[82]:


customer_name = "John"
pin = "1234"

in_name = input("Enter your name: ")
in_pin = input("Enter your pin:  ")

if in_name == customer_name and in_pin == pin:
    print("Welcome to all your bank stuff! ")
else: 
    print("we eat money! - wrong pin!")


# In[83]:


# OR GATE 
student_attendence  = 100
grade = 25

student_attendence == 100 or grade == 25


# In[84]:


# OR GATE 
student_attendence  = 100
grade = 25

student_attendence == 0 or grade == 100


# In[ ]:




