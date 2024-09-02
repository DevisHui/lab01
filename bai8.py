# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:34:00 2024

@author: Chi
"""

Can_nang = float(input("Nhập cân nặng của bạn(kg): "))
Chieu_cao = float(input("Nhập chiều cao của bạn(m): "))
cong_thuc_BMI = Can_nang / (Chieu_cao**2)
print("Số đo sức khỏe BMI của bạn là:",cong_thuc_BMI)
