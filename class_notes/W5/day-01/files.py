# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 19:35:39 2020

@author: platf
"""


# 'r' stands for read below - to read only

def read_data1(file_name):
    print(file_name)
    file = open(file_name, "r")
    print(file)



read_data1("data.txt")
