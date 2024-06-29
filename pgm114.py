# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:50:25 2024
display upper,lower,digit or special char. other than $
@author: arul
"""
n=input("enter character:")
while n!='$':
    print(n)
    if n>='A' and n<'Z':
        print("upper")
    elif n>='a' and n<='z':
        print("lower")
    elif n>='0' and n<='9':
        print("digit")
    else:
        print("special char.")
    n=input("enter character")