# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:09:05 2024
extract all characters from the mth position
@author: arul
"""
s1=input("enter the string: ")
m=int(input("enter m: "))
s2=''
i=m
while i<len(s1):
    s2=s2+s1[i]
    i=i+1
print(s2)