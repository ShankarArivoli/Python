# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 23:25:08 2024
upper or lower or digit or special chatacter by unicode
@author: arul
"""
x=input("enter character: ")
u=ord(x)
if u>=65 and u<=90:
    print("upper")
elif u>=97 and u<=122:
    print("lower")
elif u>=48 and u<=57:
    print("digit")
else:
    print("special character")