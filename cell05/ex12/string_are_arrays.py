#!/usr/bin/env python3
"""count lol"""
import sys
if len(sys.argv[1:]) != 1 or sys.argv[1].count('z') < 1:
    print(None)
else:
    for i in sys.argv[1]:
        print(i if i == "z" else "", end="")
