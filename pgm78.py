# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 23:35:58 2024
flip the alphabets
@author: arul
"""
a=input("enter alphabet: ")
u=ord(a)
if u>=65 and u<=90:
    x=u+32
    b=chr(x)
    print(b)
elif u>=97 and u<=122:
    y=u-32
    c=chr(y)
    print(c)
else:
    print("not an alphabet")