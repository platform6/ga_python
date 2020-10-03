import re
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:56:14 2020

@author: platf
"""
class Vowels:

    def __init__(self, str_input):
        self.str_input = str_input


    def check_vowels(self):
        each_letter = list(self.str_input)
        vowel_count = 0
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        for index, value in enumerate(each_letter):
            if value in vowel_list:
                vowel_count += 1
        return str(vowel_count)

class StringCount:

    def __init__(self, str_input):
        self.str_input = str_input

    # commented out code returns 1 w/ test string 'azcbobobegghakl'
    # def find_bob(self):
    #     str_to_eval = self.str_input
    #     char_set = 3
    #     count = 0
    #     new_list = [str_to_eval[i: i + char_set] for i in range(0, len(str_to_eval), char_set)]
    #     for index, value in enumerate(new_list):
    #         print(value)
    #         if value == 'bob':
    #             count += 1
    #     return str(count)

    # def find_bob(self):
    #     return len(re.findall("bob", self.str_input))

    # def find_bob(self):
    #     return self.str_input.count('bob')

    def find_bob(self):
       return str([self.str_input[i:i+3] for i in range(len(self.str_input))].count('bob'))

    #  so, why does this work?  where the other approaches gave 1 as the result
    #  if you print([self.str_input[i:i+3] for i in range(len(self.str_input))])
    #  you get ['azc', 'zcb', 'cbo', 'bob', 'obo', 'bob', 'obe', 'beg', 'egg',
    #  'ggh', 'gha', 'hak', 'akl', 'kl', 'l']

    #  so this self.str_input[i:i+3] is giving a split string starting at index 0 to 3
    #  (not inclusive of 3, so 0,1,2)
    #  then incrementing up each loop to get the overlapping strings
    #  the loop is limited by the range() to the lenght of the string
    #  then the .count() method evaluates the list for the bob occurrences

class StringReversal:

    def __init__(self, str_input):
        self.str_input = str_input

    def reversed_string(self):
        rev_str = ''
        for i in range(len(self.str_input)):
            rev_str = rev_str + self.str_input[-(i+1)]
        return rev_str

    #  rev_str is the instance variable
    #  the for loop is limited the length of the objects str_input
    #  each loop the string variable adds a characeter starting at
    #  negaitve i + 1, so the first loop i = 0 and i + 1 = 1 and the
    #  negative sign indicates the first index from the last
    #  and then the incrementing i will grab each character at index from last
    #  to first

class UpperLower:

    def __init__(self, str_input):
        self.str_input = str_input

    def count_upper_lower(self):
        upper = 0
        lower = 0
        new_list = list(self.str_input)
        for index, value in enumerate(new_list):
            if value.isupper():
                upper += 1
            else:
                lower += 1
        return "UPPERCASE: "+str(upper)+", LOWERCASE: "+str(lower)+"."













#  Start test cases and problem descriptions below \/

#  Write a program that counts up the number of vowels contained
#  in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#  For example, if s = 'azcbobobegghakl', your program should print:
#  Number of vowels: 5

question1 = Vowels("Hello World")
print("Number of vowels: " + question1.check_vowels())

#  Write a program that prints the number of times the string 'bob' occurs in
#  s. For example, if s = 'azcbobobegghakl', then your program should print
#  Number of times bob occurs is: 2

question2 = StringCount("HelloWorldbobsureshbosigerabob")
print("Number of times bob occurs is: " + question2.find_bob())

#  Ask the user to input a string and then reversal the given input. Input:
#  "Programming in Python" Output: nohtyP ni gnimmargorP

question3 = StringReversal("Programming in Python")
print(question3.reversed_string())

#  Write a program that accepts a sentence and calculate the number of
#  uppercase letters and lowercase letters. Suppose the following input is
#  supplied to the program. Input: Hello World Output: UPPERCASE: 2,
#  LOWERCASE: 9. You may count space as lowercase.

question4 = UpperLower("Hello World")
print(question4.count_upper_lower())
