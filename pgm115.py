# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:55:52 2024
count upper, lower, digit, special char. other than $
@author: arul
"""
a=0
b=0
c=0
d=0
n=input("enter character:")
while n!='$':
    print(n)
    if n>='A' and n<'Z':
        a=a+1
    elif n>='a' and n<='z':
        b=b+1
    elif n>='0' and n<='9':
        c=c+1
    else:
        d=d+1
    n=input("enter character")
print(a)
print(b)
print(c)
print(d)