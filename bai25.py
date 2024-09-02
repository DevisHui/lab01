# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:59:08 2024

@author: Chi
"""

chc= input("Nhập một chữ cái: ")
if chc.islower():
    chc = chc.upper()
else:
    chc = chc.lower()
print("Kết quả:",chc)