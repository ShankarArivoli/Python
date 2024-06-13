# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:50:29 2024
pallindrom or not
@author: arul
"""
n=int(input("enter n: "))
x=n%10
a=n//10
y=a%10
z=a//10
b=x*100
c=y*10
d=z*1
r=b+c+d
if n==r:
    print("pallindrom")
else:
    print("not a pallindrom")