# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:32:12 2024

@author: Chi
"""

Hinh = input("Nhập vào hình (vuông),(chữ nhật),(tròn): ")
if Hinh == 'vuông':
    canh = float(input("Nhập chiều dài cạnh: "))
    chu_vi = 4*canh
    print("Chu vi hình vuông là:",chu_vi)
    dien_tich = canh **2
    print("Diện tích hình vuông là:",dien_tich)
elif Hinh == 'chữ nhật':
    rong = float(input("Nhập chiều rộng: "))
    dai = float(input("Nhập chiều dài: "))
    chu_vi = 2 * rong + dai
    print("Chu vi hình chữ nhật là: ",chu_vi)
    dien_tich = rong * dai
    print("Diện tích hình chữ nhật là: ",dien_tich)
elif Hinh == 'tròn':
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    chu_vi = 2 * 3.14 * ban_kinh
    print("Chu vi hình trình tròn là: ",chu_vi)
    dien_tich = 3.14 * (ban_kinh**2)
    print("Diện tích hình tròn là: ",dien_tich)
else:
    print("Hình không hợp lệ")