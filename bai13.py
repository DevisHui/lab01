# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:22:57 2024

@author: Chi
"""

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
print(f"{ngay}/{thang}/{nam}")
print(f"{ngay}/{thang}/{str(nam)[-2:]}")
print(f"{nam}/{ngay}/{thang}")
ngay , thang , nam = map(int, input("Nhập lại theo định dạng ngày/tháng/năm: ").split('/'))
print(f"{ngay}/{thang}/{nam}")
print(f"{ngay}/{thang}/{str(nam)[-2:]}")
print(f"{nam}/{ngay}/{thang}")