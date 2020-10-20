# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:22:53 2020

@author: platf
"""

import os

def read_csv_data(file_name):

    #  os.path.abspath(__this__) = current working file
    #  os.path.dirname() = current dir where the file is contained.

    data = {}

    try:
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, file_name)


        file = open(file_path, "r")


        for line in file:

            column = line.split(',')

            data[column[0].rstrip("\n")] = [column[1], column[2], float(column[3]), float(column[4])]

        file.close()

    except:
        print("-------------File can not be found-------------")

    return data


all_data = read_csv_data("bank-data.csv")


print(all_data)