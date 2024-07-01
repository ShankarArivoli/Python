# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:22:57 2024
read and count the vowels and non vowels
@author: arul
"""
a=0
b=0
s=input("enter the string: ")
i=0
while i<len(s):
    if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
        a=a+1
    else:
        b=b+1
    i=i+1
print(a)
print(b)        