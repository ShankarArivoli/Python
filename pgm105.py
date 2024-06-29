# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:15:10 2024
count no. of leap year
@author: arul
"""
a=int(input("enter a: "))
b=int(input("enter b: "))
x=0
c=a
while c<=b:
    print(c)
    d=c%4
    if d==0:
        x=x+1
    else:
        print("not leap year")
    c=c+1
print(x)