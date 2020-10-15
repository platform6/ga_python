# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:22:53 2020

@author: platf
"""

import os

def read_data1(file_name):

    #  os.path.abspath(__this__) = current working file
    #  os.path.dirname() = current dir where the file is contained.

    try:
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, file_name)

        # print(file_path)

        # open the file for read only mode!

        file = open(file_path, "r")


        # print each line in file
        # .rstrip("\n") removes the break lines

        for line in file:
            row = line.rstrip("\n")
            print(f'record is {row}')


        file.close()   # terminate the bond between the file object and the object itself
    except:
        print("-------------File can not be found-------------")

read_data1("data123.txt")