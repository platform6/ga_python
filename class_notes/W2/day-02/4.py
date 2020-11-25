# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:15:30 2020

@author: platf
"""

def foo (a, b, c):
    print(a)
    print(b)
    print(c)
    

foo (10, 20, 30)

print()


#  setting default values
#  any variable after the first default value must also have a default value

def foo (a, b = 10, c = 33):
    print(a)
    print(b)
    print(c)
    

foo (10)

print()


#  everything after the first two positional arguemets will be
#  sent to *args

def foo(a, b, *args):
    print('a is ', a)
    print('b is', b)
    print('some_args is', args)
    

foo('first', 'second', 'more', 'and more')

print()

# **kwargs = keyword argument values - creates key and value pairs as dictionary

def foo(**kwargs):
    print(kwargs)
    
foo(name = 'suresh',
    age = '22')

print()


# args and kwargs always come at the end of the list of parameters
# args = tuple
# kwargs = dictionary

def foo_final(required_param, default = 'default', *args, **kwargs):
    print(required_param)
    print(default)
    print(args)
    print(kwargs)
    
foo_final(10, 100,0,1,2,True,5,6,name = "john")


print()


def mean_cal(**kwargs):
    subject_list = []
    sum_score = 0
    
    for subject, score in kwargs.items():
        subject_list.append(subject)
        sum_score += score
        
    student_mean = sum_score/ len(subject_list)
    print(subject_list)
    print(student_mean)
    

mean = mean_cal(math = 100, english = 90, history = 85)

