# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:11:06 2024
count no.of even and odd no.
@author: arul
"""
a=int(input("enter a: "))
b=int(input("enter b: "))
x=0
y=0
c=a
while c<=b:
    print(c)
    d=c%2
    if d==0:
        x=x+1
    else:
        y=y+1
    c=c+1
print(x)
print(y)