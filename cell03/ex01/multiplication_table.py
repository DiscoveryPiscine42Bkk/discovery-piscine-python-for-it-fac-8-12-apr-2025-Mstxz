#!/usr/bin/env python3
"""just a normal multiplication table"""
num = int(input("Enter a number\n"))

for i in range(10):
    print(f"{i} x {num} = {i*num}")
