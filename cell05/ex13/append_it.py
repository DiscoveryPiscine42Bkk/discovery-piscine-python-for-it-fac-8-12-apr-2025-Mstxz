#!/usr/bin/env python3
"""append it btw"""
import sys
import re
data = sys.argv[1:]
new = []
if data is None:
    print(None)
else:
    for i in data:
        if re.findall("ism",i):
            continue
        i += "ism"
        print(i)
