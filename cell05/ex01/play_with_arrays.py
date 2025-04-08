#!/usr/bin/env python3
"""bro just traverse"""
arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
print("Original array:",arr)
for i in arr:
    i += 2
    new_arr.append(i)
print("New array:",new_arr)
