# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:39:23 2024
single or two or three or four digit no.
@author: arul
"""
n=int(input("enter n: "))
if n>=0 and n<=9:
    print("single digit no.")
elif n>=10 and n<=99:
    print("double digit no.")
elif n>=100 and n<=999:
    print("three digit no.")
elif n>=1000 and n<=9999:
    print("four digit no.")
else:
    print("more than 4 digits")