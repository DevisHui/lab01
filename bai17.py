# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:42:16 2024

@author: Chi
"""

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
so_nguyen_lon_nhat = max(a, b, c)
so_nguyen_nho_nhat = min(a, b, c)
print("Số nguyên lớn nhất",so_nguyen_lon_nhat)
print("Số nguyên nhỏ nhất",so_nguyen_nho_nhat)
