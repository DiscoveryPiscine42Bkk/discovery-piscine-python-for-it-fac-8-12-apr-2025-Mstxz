#!/usr/bin/env python3
"""bro just traverse"""
arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = set()
print(arr)
for i in arr:
    if i < 5:
        continue
    i += 2
    new_arr.add(i)
print(new_arr)
