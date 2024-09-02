# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:33:33 2024

@author: Chi
"""

gio = int(input("Nhập số giờ: "))
phut = int(input("Nhập số phút: "))
gi = int(input("Nhập số giây: "))
tinh_so_giay = gio * 3600 + phut * 60 + gi
print("tổng số giây", tinh_so_giay)