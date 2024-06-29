# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:37:28 2024
sum of +ve,-ve, other than 1000
@author: arul
"""
a=0
b=0
n=int(input("enter n:"))
while n!=1000:
    print(n)
    if n>0:
        a=a+n
    elif n<0:
        b=b+n
    else:
        print("zero")
    n=int(input("enter n:"))
print(a)
print(b)