#!/usr/bin/env python3
"""bro use len() trust me"""
import sys

def gotolooptho(a):
    """loop it tho"""
    print(f"parameters: {len(a)}")
    for i in a:
        print(f"{i}: {len(i)}")

if sys.argv[1:] is None:
    print(None)
else:
    gotolooptho(sys.argv[1:])
