# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 23:22:58 2024
digit or not using unicode
@author: arul
"""
x=input("enter character")
u=ord(x)
if u>=48 and u<=57:
    print("digit")
else:
    print("not a digit")