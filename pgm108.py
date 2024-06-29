# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:24:36 2024
biggest no. other than 1000
@author: arul
"""
m=0
n=int(input("enter n:"))
while n!=1000:
    print(n)
    if n>m:
        m=n
    else:
        n=int(input("enter n:"))
print(m)