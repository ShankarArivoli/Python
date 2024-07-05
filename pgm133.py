# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:16:06 2024
extract last n characters
@author: arul
"""
s1=input("enter the string: ")
n=int(input("enter n: "))
s2=''
i=len(s1)-n
while i<len(s1):
    s2=s2+s1[i]
    i=i+1
print(s2)