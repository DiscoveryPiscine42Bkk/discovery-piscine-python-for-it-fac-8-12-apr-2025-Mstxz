#!/usr/bin/env python3
"""just range var"""
import sys
data = sys.argv[1:]
if data is None or len(data) != 2:
    print(None)
else:
    pr = list(range(int(data[0]), int(data[1]) + 1))
    print(pr)
