# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:19:26 2024
reverse the string
@author: arul
"""
s1=input("enter s1: ")
s2=''
i=len(s1)-1
while i>=0:
    s2=s2+s1[i]
    i=i-1
print(s2)