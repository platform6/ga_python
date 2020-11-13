# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:35:15 2020

@author: platf
"""

from py_thesaurus import Thesaurus

input_word = "fire"

new_word = Thesaurus(input_word)

print(new_word.get_synonym())


