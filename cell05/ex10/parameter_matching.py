#!/usr/bin/env python3
"""another parameter lol"""
import sys
if sys.argv[1:] is None:
    print(None)
else:
    msg = input("What was the parameter? ")
    print("Good job!" if msg == sys.argv[1] else "Nope, sorry...")