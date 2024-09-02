# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:50:55 2024

@author: Chi
"""

gio1 = int(input("Nhập giờ một: "))
gio2 = int(input("Nhập giờ hai: "))
phut1 = int(input("Nhập phút một: "))
phut2 = int(input("Nhập phút hai: "))
giay1 = int(input("Nhập giây một: "))
giay2 = int(input("nhập giây hai: "))
gio_cong_gio = gio1 + gio2
gio_tru_gio = gio1 - gio2
phut_cong_phut = phut1 + phut2
phut_tru_phut = phut1 - phut2
giay_cong_giay = giay1 + giay2
giay_tru_giay = giay1 - giay2
print(f"Kết quả cộng: Giờ {gio_cong_gio}, Phút {phut_cong_phut}, Giây {giay_cong_giay}")
print(f"Kết quả trừ : Giờ {gio_tru_gio}, Phút {phut_tru_phut}, Giây {giay_tru_giay}")