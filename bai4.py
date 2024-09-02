# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:58:54 2024

@author: Chi
"""

N = int(input("Nhập số nguyên dương có 2 chữ số: "))
if 10<=N<=99:
    Hang_chuc = N // 10
    Hang_don_vi = N % 10
    Tong_chu_so = Hang_chuc + Hang_don_vi
    print("Tổng các chữ số của N là",Tong_chu_so)
else:
    print("Số nhập vào không phải là số nguyên dương có 2 chữ số")


    