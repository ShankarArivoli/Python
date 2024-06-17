# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:59:20 2024
print ----*
      ---**
      --***
      -****
      *****
      -****
      --***
      ---**
      ----*
@author: arul
"""
n=4
m=1
i=1
while i<=5:
    j=1
    while j<=n:
        print('-',end='')
        j=j+1
    k=1
    while k<=m:
        print('*',end='')
        k=k+1
    i=i+1
    n=n-1
    m=m+1
    print()
a=1
b=4
x=1
while x<=4:
    y=1
    while y<=a:
        print('-',end='')
        y=y+1
    z=1
    while z<=b:
        print('*',end='')
        z=z+1
    x=x+1
    a=a+1
    b=b-1
    print()