# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:16:55 2024
print non vowels in the string
@author: arul
"""
s='LINSOFT ACADEMY'
i=0
while i<len(s):
    if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
        pass
    else:
        print(s[i])
    i=i+1