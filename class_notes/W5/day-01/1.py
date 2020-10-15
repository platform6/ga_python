# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:09:27 2020

@author: platf
"""

class Slideshow:

    def __init__(self):
        self.__slide_qty = 0

    def __get_slide_qty(self):
        return self.__slide_qty

    def __set_slide_qty(self, value):
        self.__slide_qty = value


    number_of_slides = property(fget = __get_slide_qty, fset = __set_slide_qty)


class Person:

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        print(f"Welcome to {self.name}, your user ID is {self.user_id}")


# Speaker is a Person - Speaker hasa  Slideshow

class Speaker(Person):

#Example of a   HAS - A   relationship  as opposed to a   IS - A relationship

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.slide_show = Slideshow()
        self.slide_show.number_of_slides = 40
        super().__init__(self.name, self.user_id)


    def get_full_info(self):
        return f"Speaker {self.name} has a slideshow with {self.slide_show.number_of_slides} slides"


guest_speaker = Speaker("Holden",1001)

print(guest_speaker.get_full_info())
