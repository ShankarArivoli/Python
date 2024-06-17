# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:36:41 2024
print 5 colums of ***.......*
@author: arul
"""
n=int(input("enter n:"))
i=1
while i<=5:
    j=1
    while j<=n:
        print('*', end='')
        j=j+1
    i=i+1
    print()