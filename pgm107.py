# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:21:34 2024
read and find the sum of no.s other than 1000
@author: arul
"""
a=0
n=int(input("enter n:"))
while n!=1000:
    print(n)
    a=a+n
    n=int(input("enter n:"))
print(a)