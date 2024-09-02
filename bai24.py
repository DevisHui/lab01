# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:54:23 2024

@author: Chi
"""

gio = int(input("Nhập số giờ: "))
phut = int(input("Nhập số phút: "))
gi = int(input("Nhập số giây: "))
if 0<= gio <=23 and 0 <= phut <= 59 and 0<= gi <=59:
    print("Thời gian hợp lệ")
else:
    print("Thời gian không hợp lệ")
    