# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:50:26 2020

@author: platf
"""

class Phone:

    def __init__(self, phone_number):
        self.number = phone_number

    def call(self, other_number):
        print(f"Calling from {self.number} to {other_number}")

    def text(self, other_number, msg):
        print(f"Texting from {self.number} to {other_number} print {msg}")


class IPhone(Phone):

    def __init__(self, phone_number):
        self.finger_id = None
        super().__init__(phone_number)

    def set_fingerprint(self, finger_id):
        self.finger_id = finger_id
        print(f"Fingerprint id = {finger_id}")

    def unlock(self, fingerprint):
        if self.finger_id == fingerprint:
            print("Unlocked")

class Android(Phone):

    def __init__(self, phone_number):
        self.keyboard = None
        super().__init__(phone_number)

    def set_keyboard(self, keyboard):
        self.keyboard = keyboard
        print(f"Keyboard set to {keyboard}")




iphone6 = IPhone(3476781232)
iphone6.set_fingerprint(1121)
iphone6.unlock(1121)
iphone6.call(3476781233)
iphone6.text(3476781233, "I'm on my way :)")


androidPhone = Android(3476781232)
androidPhone.set_keyboard("Default")
androidPhone.call(3476781233)
androidPhone.text(3476781233, "I'm on my way :)")