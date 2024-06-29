# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:31:17 2024
count the positive, negative and zero other than 1000
@author: arul
"""
a=0
b=0
n=int(input("enter n:"))
while n!=1000:
    print(n)
    if n>0:
        a=a+1
    elif n<0:
        b=b+1
    else:
        pass
    n=int(input("enter n:"))
print("no. of positive:",a)
print("no. of negative:",b)