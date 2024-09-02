# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:04:47 2024

@author: Chi
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
if a >= b and a >=c:
    so_lon_nhat = a
elif b >= a and b >=c:
    so_lon_nhat = b
else: so_lon_nhat = c
print("Số lớn nhất",so_lon_nhat)