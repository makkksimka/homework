# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

month = int(input())

if month > 12 or month < 1:
    print("Incorrect input")
elif 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Autumn")
else:
    print("Winter")