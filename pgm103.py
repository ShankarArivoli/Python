# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:06:45 2024
count even no. b/w limits
@author: arul
"""
a=int(input("enter a: "))
b=int(input("enter b: "))
e=0
c=a
while c<=b:
    print(c)
    d=c%2
    if d==0:
        e=e+1
    else:
        print("odd")
    c=c+1
print(e)