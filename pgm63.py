# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:48:55 2024
leap year or not using not
@author: arul
"""
n=int(input("enter n: "))
a=n%4
if not a:
    print("leap year")
else:
    print("not leap year")