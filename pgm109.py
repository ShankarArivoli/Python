# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:27:57 2024
+ve, -ve, or zero other than 1000
@author: arul
"""
n=int(input("enter n:"))
while n!=1000:
    print(n)
    if n>0:
        print("positive")
    elif n<0:
        print("negative")
    else:
        print("zero")
    n=int(input("enter n:"))