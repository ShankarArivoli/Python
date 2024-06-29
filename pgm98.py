# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:55:52 2024
print      *
          * *
         *   *
        *     *
       *       *
      ***********
@author: arul
"""
f=1
while f<=6:
    print(' ',end='')
    f=f+1
print('*')
n=5
m=1
i=1
while i<=5:
    j=1
    while j<=n:
        print(' ',end='')
        j=j+1
    print('*',end='')
    k=1
    while k<=m:
        print(' ',end='')
        k=k+1
    print('*')
    i=i+1
    n=n-1
    m=m+2
c=1
while c<=13:
    print('*',end='')
    c=c+1