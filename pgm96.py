# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 12:10:38 2024
print 1
     123
    12345
   1234567
  123456789
   1234567
    12345
     123
      1
@author: arul
"""

n=4
m=1
i=1
while i<=5:
    j=1
    while j<=n:
        print(' ',end='')
        j=j+1
    k=1
    while k<=m:
        print(k,end='')
        k=k+1
    i=i+1
    n=n-1
    m=m+2
    print()
a=1
b=7
x=1
while x<=4:
    y=1
    while y<=a:
        print(' ',end='')
        y=y+1
    z=1
    while z<=b:
        print(z,end='')
        z=z+1
    x=x+1
    a=a+1
    b=b-2
    print()