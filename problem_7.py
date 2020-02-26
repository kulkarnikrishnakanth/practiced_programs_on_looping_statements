# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:43:56 2020

@author: DW4
"""
num = []
for i in range(100,401):
    s = str(i)
    if (int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0):
        num.append(int(s))
print(num)