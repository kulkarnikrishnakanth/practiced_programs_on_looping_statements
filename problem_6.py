# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:24:40 2020

@author: DW4
"""

num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2st number: "))
if num1 > num2:
    smaller = num2
else:
    smaller = num1
for i in range(1, smaller+1):
    if((num1 % i == 0)) and (num2 % i == 0):
        hcf = i
print("HCF is: ",hcf)
