# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:07:14 2020

@author: DW4
"""

lower = int(input("enter lower range: "))
upper = int(input("enter upper range: "))
for num in range(lower, upper+1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num)
