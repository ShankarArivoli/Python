# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:42:46 2024
convert upper to lower and then extract
@author: arul
"""
s1=input("enter the string:")
s2=''
i=0
while i<len(s1):
    if s1[i]>='A' and s1[i]<='Z':
        u=ord(s1[i])
        x=u+32
        a=chr(x)
        s2=s2+a
    else:
        s2=s2+s1[i]
    i=i+1
print(s2)    