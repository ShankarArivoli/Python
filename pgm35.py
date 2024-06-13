# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:30:09 2024
sum and product of the digits of 3 digit no.
@author: arul
"""
n=int(input("enter n: "))
x=n%10
a=n//10
y=a%10
z=a%10
s=x+y+z
p=x*y*z
print(s)
print(p)