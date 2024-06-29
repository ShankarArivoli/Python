# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 09:58:36 2024
1 - 100 even or odd
@author: arul
"""
c=1
while c<=100:
    print(c)
    a=c%2
    if a==0:
        print("even")
    else:
        print("odd")
    c=c+1