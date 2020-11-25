# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:30:09 2020

@author: platf
"""

class VowelCounter:

    def __init__(self):
        self.__str_input = None

    def __set_string(self, str_input):
        self.__str_input = str_input

    def __get_string(self):
        return self.__str_input

    def check_vowels(self):
        each_letter = list(self.__str_input)
        vowel_count = 0
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        for index, value in enumerate(each_letter):
            if value in vowel_list:
                vowel_count += 1
        return str(vowel_count)

    string = property(fset = __set_string, fget = __get_string)

class SortWords:

    def __init__(self):
        self.__unsorted_words = None
        self.__sorted_words = None

    def __set_words(self, list_input):
        self.__unsorted_words = list_input

    def __get_words(self):
        return self.__sorted_words

    def sort_words(self):
        self.__sorted_words = sorted(self.__unsorted_words, key = str.lower)


    words = property(fset = __set_words, fget = __get_words)

class Reverser:

    def __init__(self):
        self.__mirror = None

    def __set_mirror(self, str_input):
        self.__mirror = str_input

    def __get_mirror(self):
        rev_str = ''
        for i in range(len(self.__mirror)):
            rev_str = rev_str + self.__mirror[-(i+1)]
        return rev_str

    string = property(fset = __set_mirror, fget = __get_mirror)



exercise1 = VowelCounter()
exercise1.string = 'Hi there!'
print(exercise1.check_vowels())
# the above should print "3"
exercise1.string = 'abracadabra'
print(exercise1.check_vowels())
# the above should print "5"

exercise2 = SortWords()
exercise2.words = ["hello", "world", "i", "am", "here"]
exercise2.sort_words()
# should print '["am","hello","here","i","world"]'
print(exercise2.words)
# should print the original list!
exercise2.words = ["oh","please","let","these","words","sort"]
print(exercise2.sort_words())
# should print '["let","oh","please","sort","these","words"]
print("==============\n")

exercise3 = Reverser()
exercise3.string = "Howdy!"
print(exercise3.string)
# should print "!ydwoH"
exercise3.string = "OK bye!"
print(exercise3.string)
# should print "!eyb KO"


