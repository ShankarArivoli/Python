# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 23:18:26 2024
upper case or not by unicode
@author: arul
"""
x=input("enter character: ")
u=ord(x)
if u>65 and u<=90:
    print("upper")
else:
    print("not upper")