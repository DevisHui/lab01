# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:49:01 2024

@author: Chi
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))
if a <=b and a<=c and a <=d:
    so_be_nhat = a
elif b <= a and b <=c and b <=d:
    so_be_nhat = b
elif c <=a and c <=b and c <=d:
    so_be_nhat = c
elif d <=a and d <= b and d <=c:
    so_be_nhat = d
print("Số bé nhất",so_be_nhat)
        
    
        