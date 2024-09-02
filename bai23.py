# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:47:06 2024

@author: Chi
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
delta = b*b - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta ==0:
    print("Phương trình có nghiệm kép: x1 = x2",-b/(2*a))
else: import math
x1 = ( -b + math.sqrt(delta)) / (2*a)
x2 = ( -b - math.sqrt(delta)) / (2*a)
print("Phương trình có 2 nghiệm phân biệt: ")
print("x1=",x1,"x2=",x2)
        
