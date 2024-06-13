# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:31:03 2024
arithmatic or relational or logical or other
@author: arul
"""
n=input("enter operator: ")
if n=='+' or n=='*' or n=='/' or n=='//' or n=='%' or n=='**':
    print("arithmatic operator")
elif n=='>' or n=='<' or n=='>=' or n=='<=' or n=='==' or n=='!=':
    print("relational operator")
elif n=='and' or n=='or' or n=='not':
    print("logical")
else:
    print("other operator")