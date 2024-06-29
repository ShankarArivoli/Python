# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 11:08:02 2024
biggest of 10 no.s
@author: arul
"""
m=0
c=1
while c<=10:
    n=int(input("enter n:"))
    if n>m:
        m=n
    else:
        pass
    c=c+1
print(m)