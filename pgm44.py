# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:45:01 2024
leap year or not
@author: arul
"""
n=int(input("enter n: "))
r=n%4
if r==0:
    print("leap year")
else:
    print("not a leap year")