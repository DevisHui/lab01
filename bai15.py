# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:33:07 2024

@author: Chi
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
tính_biểu_thức = (((a+b) / ((a)**(1/3)+((b)**(1/3)))) - (a*b)**(1/3)) / ((((a**(1/3)) - (b**(1/3))))**2)
print("Kết quả là", tính_biểu_thức)