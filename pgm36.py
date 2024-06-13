# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:33:47 2024
reverse the given 3 digit no.
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
print(r)