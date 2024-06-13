# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 23:02:32 2024
biggest of 3 integers using ternary expression
@author: arul
"""
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
d=a if a>b else b
e=d if d>c else c
print(e)