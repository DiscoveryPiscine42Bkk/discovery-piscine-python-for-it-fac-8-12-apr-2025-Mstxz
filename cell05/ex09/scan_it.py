#!/usr/bin/env python3
"""re is kinda good tho"""
import sys
import re #stupid pep-8 is killing me
li = sys.argv[1:]
if len(li) < 2:
    print(None)
else:
    print(len(re.findall(li[0], li[1])))
