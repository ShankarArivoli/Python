# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:26:23 2024
count upper, lower, digit or special character
@author: arul
"""
a=0
b=0
c=0
d=0
s=input("enter string:")
i=0
while i<len(s):
    if s[i]>='A' and s[i]<='Z':
        a=a+1
    elif s[i]>='a' and s[i]<='z':
        b=b+1
    elif s[i]>='0' and s[i]<='9':
        c=c+1
    else:
        d=d+1
    i=i+1
print(a)
print(b)
print(c)
print(d)