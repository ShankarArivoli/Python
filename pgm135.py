# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:21:44 2024
reverse the string and check palindrome
@author: arul
"""
s1=input("enter string: ")
s2=''
i=len(s1)-1
while i>=0:
    s2=s2+s1[i]
    i=i-1
print(s2)
if s2==s1:
    print("palindrome")
else:
    print("not palindrome")