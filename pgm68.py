# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 23:11:48 2024
biggest of 3 no.s using nested ternary
@author: arul
"""
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
d=(a if a>c else c) if a>b else (b if b>c else c)
print(d)