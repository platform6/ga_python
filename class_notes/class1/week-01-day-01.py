#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello world!")


# In[4]:


print("Hello world!")


# In[5]:


# this is a single line comment! 
x = input()
x += 1
print(x)


# In[6]:


# this is a single line comment! 
x = int(input())
x += 1
print(x)


# In[7]:


#  this is a single line comment!
first_name = "Garrett"
print(first_name)


# In[8]:


print(first_name)


# In[9]:


type(first_name)


# In[10]:


type(x)


# In[11]:


#  str means string
#  we can use '' or "" to create string variables


# In[12]:


age = "11"


# In[13]:


int_age = 11


# In[14]:


type(age)


# In[15]:


type int_age


# In[16]:


type(int_age)


# In[17]:


height = 5.11


# In[18]:


price = 11.66 #  recognizes data type


# In[19]:


x = height + price


# In[20]:


print(x)


# In[ ]:


msg = 'Helllloooo wooorllld'


# In[21]:


lent(msg)


# In[22]:


len(msg)


# In[23]:


msg = 'Helllloooo wooorllld'


# In[24]:


len(msg)


# In[25]:


msg[0]


# In[26]:


msg[4]


# In[27]:


msg[4] + msg[10]


# In[28]:


msg[4] + msg[12]


# In[29]:


msg[-2]


# In[30]:


#  negative numbers in the bracket string notation will go from end of string and bring back 
#  that index -1 being the last -2 being the penultimate index


# In[31]:


#  string slicing


# In[32]:


msg


# In[33]:


msg[1:]
#  give me everything but the first letter!! 


# In[34]:


# grab everything past the first (0) index -- skipping the first letter


# In[35]:


msg[:3]   #  this is everything before the specified index - so the opposite of above!


# In[36]:


msg[3:]


# In[37]:


msg[0:3] #  give me 0 through 3 -- can remove 0 to get the same output (python defaults to 0)


# In[38]:


msg[1:7]


# In[39]:


fruit = "apple"


# In[41]:


fruit.upper() #  converts everything to upper case!


# In[42]:


fruit[0].upper()


# In[44]:


fruit[0].upper() + fruit[1:5] # capitalize the first letter


# In[45]:


dir(fruit)


# In[46]:


age = 22


# In[47]:


dir(age)  #   lists all the methods available to the integer object/


# In[48]:


# variable acts as a storage unit to store in the computers memory


# In[ ]:


# an object is something that is in the computer memory 
# using type() returns the data type that is associated with that data object
# indexing is to retrieve information using the square brackets []  a single unit of information
# 

