# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:07:22 2024
print *******
       *****
        ***
         *
@author: arul
"""
n=0
m=7
i=1
while i<=5:
    j=1
    while j<=n:
        print(' ',end='')
        j=j+1
    k=1
    while k<=m:
        print('*',end='')
        k=k+1
    i=i+1
    n=n+1
    m=m-2
    print()