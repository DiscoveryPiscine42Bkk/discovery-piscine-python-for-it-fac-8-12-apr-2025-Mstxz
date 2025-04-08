#!/usr/bin/env python3
"""adv multiplication???"""
import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    j = 0
    countj = 0
    while i <= 10:
        print(f"Table de {i}: ", end="")
        while countj <= 10:
            print(j, end=" ")
            j += i
            countj += 1
        i += 1
        j = 0
        countj = 0
        print()
