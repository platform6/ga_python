# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:38:04 2020

@author: platf
"""


# data = {
#     10001:
#             {
#             'first_name': 'Chris',
#             'last_name': 'Herzog',
#             }
#         }




# data2 = {
#     10002: {
#     'first_name': 'Garrett',
#     'last_name' : 'Conn',
#     }
#    }




# data2[10003] = ["Garrett", "Conn", "password", 0, 0]

# print(data2)




my_dict = {'10001': ['suresh', 'sigera', 'juagw362', 1000.0, 10000.0], '10002': ['james', 'taylor', 'idh36%@#FGd', 10000.0, 10000.0], '10003': ['melvin', 'gordon', 'uYWE732g4ga1', 2000.0, 20000.0], '10004': ['stacey', 'abrams', 'DEU8_qw3y72$', 2000.0, 20000.0], '10005': ['jake', 'paul', 'd^dg23g)@', 100000.0, 100000.0], '10006': ['Garrett', 'Conn', 'dlfj', 0, 0]}

# key = list(my_dict.keys())

# my_list = []
# semi_sep_list = ""
# for index, value in enumerate(my_dict.values()):
#     my_list = value
#     for item in my_list:
#         print(item)


# key_list = []
# for keys in my_dict:
#     key_list.append(keys)

# print(key_list)


for key, value in my_dict.items():
    print(key)
    for item in value:
        print(item)




