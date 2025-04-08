#!/usr/bin/env python3
"""guys, just traverse"""
import sys
li = sys.argv[1:]
if len(li) < 2:
    print(None)
else:
    for i in range(len(sys.argv[1:]), 0, -1):
        print(li[i-1])
