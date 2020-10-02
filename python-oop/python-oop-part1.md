# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python OOP 

| Title | Type | Duration | Author | 
| -- | -- | -- | -- |
| Classes - Part1 | Lesson | 2:50 | Suresh Melvin Sigera |

## Objectives
- Work with Python classes
- Use getter and setter methods in Python
- Demonstrate how to implement OOP techniques such as inheritance and polymorphism
- Employ the SOLID design patterns to follow OOP best practices

## What is OOP?
One of the defining attributes of the Python programming language, in addition to readability, is how it implements object-oriented programming (OOP) techniques.
OOP facilitates writing code in a way that allows you to think about, and model, the concepts that you are working with in your program. 

## What is an object?
In object-oriented programming, the fundamental unit is the object. An object is an entity that serves as a container for data and also controls access to the data. Associated with an object is a set of attributes, which are essentially no more than variables belonging to the object. Also associated with an object is a set of functions that provide an interface to the functionality of the object, called methods.

## What is a class
Classes are the foundation of object-oriented programming (OOP). Since everything in Python is an object, even a basic Hello, World! example makes use of OOP.
In other words, classes are abstract templates for objects. You can also say that objects are instances of classes. 
Classes contain the template for a set of behaviors (such as methods) and data (such as variables).

<p align="center">
    <img src="https://git.generalassemb.ly/SEIR-224/Python-Django/blob/master/lessons/images/python-oop-part1-1.jpg" width="400">
    <br>
    <b>Class is a blue print</b>
</p>

Let's imagine that you're building a house. One of the first tasks you'd most likely do is build a blueprint for the house. This blueprint would contain attributes and features of the house, such as these:

- The dimensions for each room
- How the plumbing will flow
- Essentially, every attribute/feature of the house

Now let me ask a dumb question. Is the blueprint of the house the actual house? No, it simply lists out the attributes and design elements for how the home will be created.

## Instance
So after the blueprint is completed, the actual home can be built. Dare I say that the home can be instantiated?
<p align="center">
    <img src="https://git.generalassemb.ly/SEIR-224/Python-Django/blob/master/lessons/images/python-oop-part1-2.jpg" width="300">
    <br>
    <b>Instance of a class</b>
</p>

<p align="center">
    <img src="https://git.generalassemb.ly/SEIR-224/Python-Django/blob/master/lessons/images/python-oop-part1-3.jpg" width="300">
    <br>
    <b>Another instance of a class</b>
</p>

## Instance methods
Instance methods are methods that are available on a specific instance or object of a class. Instances have states that are held in instance variables. As you would expect, instance methods have access to these instance variables.

## Creating a class
Here is an example of how we can create a House class to do this:
```Python
class House:
    pass
```

## Creating methods
Here we've created the base template for a house by using the class keyword and have given it the name House. 
Based on what we've learned so far, we can tell right off the bat that we have a House class with the following methods: set_address, open_door, and close_door.
```Python
class House:
    def set_address(self):
        print("setting address")

    def open_doors(self):
        print("open door")

    def close_door(self):
        print("close door")

```

## Instantiation of an object
So after the blueprint is completed, the actual home can be built. Dare I say that the home can be instantiated?

```Python
class House:
    def set_address(self):
        print("setting address")

    def open_doors(self):
        print("open door")

    def close_door(self):
        print("close door")


my_house = House()
your_house = House()

my_house.open_doors()
your_house.close_door()
```

## Instance variables
As the name suggests, instance variables are available to a particular instance. There is a specific syntax to set instance variables, you need to use the @ sign to define a variable.
A local variable that is defined inside one method, for example, cannot be accessed by another method. In order to get around this limitation, we can use instance variables inside our Python classes.
<b>An instance variable is a variable that is accessible in any instance method in a particular instance of a class</b>.
```Python
class House:

    # constructor
    def __init__(self):
        self.this_owner = ''   # <= instance variable, or field
        self.this_address = ''  # <= instance variable, or field

    def set_owner(self, owner):  # <= instance method
        self.this_owner = owner

    def get_owner(self):  # <= instance method
        return self.this_owner

    def set_address(self, address):  # <= instance method
        self.this_address = address

    def get_address(self):  # <= instance method
        return self.this_address


my_house = House()  # <= first object
your_house = House()  # <= second object

my_house.set_address('111 main street')
print(my_house.get_address())
print(your_house.get_address())

```

## Constructors
In most object-oriented languages, there is a method that’s automatically invoked when an object of that class is created. 
Other languages call such methods <b>constructors</b>, but Python also calls them initializers because they always have the name initialize. (In Java and C++, a constructor is a method with the same name as the class name.)
```Python
class House:
    def __init__(self, owner, address):
        self.this_owner = owner
        self.this_address = address

    def get_owner(self):
        return self.this_owner

    def get_address(self):
        return self.this_address


my_house = House('Suresh', '111 main street')
your_house = House('Joe', '112 main street')

print(my_house.get_owner())
print(my_house.get_owner())

print(your_house.get_owner())
print(your_house.get_owner())

```

This initialize method will automatically be invoked when an object of that class type is created using ClassName.new. Normally the initialize method is used to assign values to the class’ main attributes, in which case it’s written to accept arguments:

## QA
<p>
<img src="https://media.giphy.com/media/Y0zKnKDozV6yXBqqUW/source.gif" width="480" height="480">
</p>
