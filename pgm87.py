# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:45:14 2024
print *
      **
      ***
      ****
      *****
      ****
      ***
      **
      *
@author: arul
"""
n=1
i=1
while i<=5:
    j=1
    while j<=n:
        print('*',end='')
        j=j+1
    i=i+1
    n=n+1
    print()
m=4
a=1
while a<=4:
    b=1
    while b<=m:
        print('*',end='')
        b=b+1
    a=a+1
    m=m-1
    print()