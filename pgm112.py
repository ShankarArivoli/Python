# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:42:10 2024
average of positive and negatives
@author: arul
"""
a=0
b=0
c=0
d=0
n=int(input("enter n:"))
while n!=1000:
    print(n)
    if n>0:
        a=a+1
        c=c+n
    elif n<0:
        b=b+1
        d=d+n
    else:
        print("zero")
    n=int(input("enter n:"))
x=c/a
y=d/b
print(x)
print(y)