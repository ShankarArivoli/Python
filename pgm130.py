# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:06:14 2024
extract first n characters
@author: arul
"""
s1=input("enter the string: ")
n=int(input("enter n: "))
s2=''
i=0
while i<n:
    s2=s2+s1[i]
    i=i+1
print(s2)