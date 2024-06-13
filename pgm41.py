# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:35:27 2024
biggest of 3 integers
@author: arul
"""
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
if a>b:
    if a>c:
        print("a is bigger")
    else:
        print("c is bigger")
else:
    if b>c:
        print("b is bigger")
    else:
        print("c is bigger")