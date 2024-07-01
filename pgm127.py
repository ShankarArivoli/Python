# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:38:52 2024
extract only vowels
@author: arul
"""
s1=input("enter string:")
s2=''
i=0
while i<len(s1):
    if s1[i]=='A' or s1[i]=='E' or s1[i]=='I' or s1[i]=='O' or s1[i]=='U':
        pass
    else:
        s2=s2+s1[i]
    i=i+1
print(s2)