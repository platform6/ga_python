# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:27:31 2020

@author: platf
"""

import os

def write_data(file_name):
    try:
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, file_name)

        file = open(file_path + '.txt', 'w')
        file.write("John\n")
        file.write("Suresh\n")
        file.write("Sharon\n")
        file.write("Melvin\n")

        file.close()

    except IOError:
        print("Can not write to the file")


write_data("demo-write")
