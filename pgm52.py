# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:00:21 2024
upper or lower or digit or special character
@author: arul
"""
x=input("enter character: ")
if x>='0' and x<='9':
    print("digit")
elif x>='A' and x<='Z':
    print("upper")
elif x>='a' and x<='z':
    print("lower")
else:
    print("special")