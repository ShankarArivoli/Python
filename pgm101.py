# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:01:08 2024
1000 - 3000 leap year ot not
@author: arul
"""
c=1000
while c<=3000:
    print(c)
    a=c%4
    if a==0:
        print("leap year")
    else:
        print("not leap year")
    c=c+1
