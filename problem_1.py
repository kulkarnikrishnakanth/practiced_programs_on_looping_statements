# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:00:10 2020

@author: DW4
"""

num = int(input('enter how many numbers: '))
total_sum = 0
for i in range(num):
    numbers = float(input('enter a number: '))
    total_sum += numbers
    avg=total_sum/num
print("average of all numbers is: ", avg)