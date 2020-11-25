# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 09:42:13 2020

@author: platf
"""

class Animal:

    def __init__(self, name, color, stuff_in_belly = [], position = 0):
        self.name = name
        self.color = color
        self.stuff_in_belly = stuff_in_belly
        self.position = 0
        self.sound = None
        self.new_friend = None
        self.friends = []

    def talk(self, sound = None):
        self.sound = sound
        if self.sound != None:
            print(f"{self.name} says {self.sound}")
        else:
            print(f"{self.name} has nothing to say right now")

    def walk(self, walk_increment):
        self.position += walk_increment
        print(f"{self.name} walked {walk_increment} steps and is now at position {self.position}.")


    def run(self, run_increment):
        self.position += run_increment
        print(f"{self.name} ran {run_increment} steps and is now at position {self.position}!")

    def is_hungry(self):
        if len(self.stuff_in_belly) < 4:
            return  True
        else:
            return False

    def eat(self, food):
        if self.is_hungry():
            self.stuff_in_belly.append(food)
            print(f"{self.name} ate {food}. Yum!")
        else:
            print(f"{self.name} doesn't want to eat {food} right now.")

    def make_friends(self, new_friend):
        if Animal in new_friend.__class__.__bases__:
            self.new_friend = new_friend.name
            self.friends.append(new_friend)
            print(f"{self.name} and {self.new_friend} are now friends!")
        else:
            print(f"{self.name} can not be friends with {new_friend}")

    def __str__(self):
        print(f"{self.name} the {self.__class__.__name__}")



class Dog(Animal):

    def __init__(self, name, color, stuff_in_belly = [], position = 0):
        super().__init__(name, color, stuff_in_belly= [], position = 0)


    def talk(self, sound = 'Bark, Bark!'):
        super().talk(sound)

    def fetch(self, item):
        print(f"{self.name} brought you {item} and is eager for your approval")

class Sheep(Animal):

    def __init__(self, name, color, stuff_in_belly = [], position = 0):
        super().__init__(name, color, stuff_in_belly = [], position = 0)
        self.is_shorn = False

    def talk(self, sound = 'Baaah Baaah!'):
        super().talk(sound)

    def shear(self):
        if self.is_shorn == False:
            print(f"{self.name} is now naked, and you have a basket of wool")
        else:
            print(f"{self.name} has already been shorn!")

class Pig(Animal):

    def __init__(self, name, color, stuff_in_belly = [], position = 0):
        super().__init__(name, color, stuff_in_belly = [], position = 0)
        self.filthieness = 0

    def talk(self, sound = 'Oink, Oink!'):
        super().talk(sound)

    def wallow(self):
        self.filthieness += 1
        if self.filthieness <= 5:
            print(f"{self.name} rolled in the muck and is now at filthieness level {self.filthieness}")
        else:
            print(f"{self.name} is already as dirty as a li'l piggy could possibly be!")

class Chicken(Animal):

    def __init__(self, name, color, stuff_in_belly = [], position = 0):
        super().__init__(name, color, stuff_in_belly = [], position = 0)
        self.eggs_layed = 0

    def lay_eggs(self, number_of_eggs):
        self.eggs_layed += number_of_eggs
        print(f"{self.name} has produced {self.eggs_layed} eggs for the farm!")

class Bull(Animal):

    def __init__(self, name, color, stuff_in_belly = [], position = 0):
        super().__init__(name, color, stuff_in_belly = [], position = 0)
        self.things_charged = []
        self.item = None

    def charge(self, item):
        self.item = item
        if len(self.things_charged) > 3:
            print(f"{self.name} is angry at EVERYTHING. He's very tired now so instead of charging {self.item}, he decided to lay down")
        else:
            self.things_charged.append(item)
            print(f"{self.name} has charged {self.item}. Wow, he's angry!")









# Test your class by creating a new variable called sparky that will
# be an instance of the Animal class, then make sure you can access sparky's
# attributes


sparky = Animal('Sparky', 'brown', ["dog food", "McDonalds wrapper"])


sparky.talk()
sparky.talk("Grrrrrrrrrrrrrr")
sparky.walk(2)
sparky.run(8)
sparky.eat("leftovers")
sparky.eat("socks")
sparky.eat("garbage")


sparky = Dog('Sparky','brown',["dog food", "McDonald's wrapper"])
print(type(sparky))   # dog object
sparky.talk()
sparky.fetch("a ball")


print(" \n " * 5)


dog = Dog("Blitzer", "yellow")

# Output the dog's attributes
print(f"Our dog's name is {dog.name}. He has {dog.color} fur.")

# Invoke some behavior
dog.talk()
dog.talk('whimper whimper')
dog.fetch('a stick')

# Walk the dog
dog.walk(4)

# Run the dog
dog.run(16)

# Feed the dog
dog.eat('pie')
dog.eat('dead woodchuck')
dog.eat('pretzels')

# Is the dog hungry?
if dog.is_hungry:
    print("He's still hungry!")
else:
    print("He's stuffed!")

# Feed the dog some more
dog.eat('bugs')
dog.eat('dog food')

print("===================")

# Create a sheep
sheep = Sheep("Shaun", "white")

# Test out some Sheep moves
sheep.talk
sheep.shear()
sheep.run(12)

print("===================")

# Create a pig
pig = Pig("Carl", "pink")

# Have your pig act very piggy
pig.wallow()
pig.talk()
pig.wallow()
pig.wallow()
pig.talk('I am so happy!')
pig.wallow()
pig.wallow()
pig.wallow()

chicken = Chicken("Tabitha the chicken", "white")

chicken.lay_eggs(10)
chicken.lay_eggs(10)

bull = Bull("Dave", "blue")

bull.charge("piano")
bull.charge("wall")
bull.charge("vending machine")
bull.charge("computer")
bull.charge("chicken")
bull.charge("vending machine")
bull.charge("computer")
bull.charge("chicken")


bull.make_friends(chicken)
bull.make_friends(pig)
bull.make_friends("Tom the farmer")


# for the Object.__class__.__bases__ in the make_friends mehtod
# it is determining if the parameters parent class is the same as
# so when you pass in a string thats base class is (<class 'object'>,)
# it does not match the base Animal class (<class '__main__.Animal'>,)
# so they can't be friends.

# __str__ implementation tests

print(" \n " * 2)

pig.__str__()
bull.__str__()
chicken.__str__()



