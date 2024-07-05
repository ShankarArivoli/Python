# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:12:06 2024
copy n characters from mth position
@author: arul
"""
s1=input("enter string: ")
n=int(input("enter n: "))
m=int(input("enter m: "))
s2=''
i=m
while i<m+n:
    s2=s2+s1[i]
    i=i+1
print(s2)