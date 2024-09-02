# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:12:48 2024

@author: Chi
"""

number_to_string={0:"không",1:"một",2:"hai",3:"ba",4:"bốn",5:"năm",6:"sáu",7:"bảy",8:"tám",9:"chín"}
a = int(input("Nhập một số bất kỳ: "))
if 0<=a<=9:
    print("Chữ số",number_to_string[a])
else:
    print("Không hợp lệ")
    