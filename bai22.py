# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:35:41 2024

@author: Chi
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
if a != 0:
    print("Phương trình có nghiệm x=", -b/a)
else:
    if b != 0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình vô số nghiệm")