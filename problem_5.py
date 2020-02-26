# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:15:49 2020

@author: DW4
"""

for num in range(1,51):
    if num %3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)