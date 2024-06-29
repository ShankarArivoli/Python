# -*- coding: utf-8 -*-
"""
Spyder Editor
print         a
             abc
            abcde
           abcdefg
            abcde
             abc
              a
This is a temporary script file.
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
        u=k+96
        r=chr(u)
        print(r,end='')
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
        v=z+96
        y=chr(v)
        print(y,end='')
        z=z+1
    x=x+1
    a=a+1
    b=b-2
    print()