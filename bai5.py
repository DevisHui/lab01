# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:36:51 2024

@author: Chi
"""

gio = int(input("Nhập số giờ: "))
phut = int(input("Nhập số phút: "))
gi = int(input("Nhập số giây: "))
tong_giay = gio * 3600 + phut * 60 + gi
print("Tổng giây",tong_giay)