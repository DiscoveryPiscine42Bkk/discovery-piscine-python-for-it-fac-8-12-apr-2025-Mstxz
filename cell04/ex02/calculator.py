#!/usr/bin/env python3
"""calc()"""
num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))

print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} / {num2} = {int(num1/num2) if num1 % num2 == 0 else num1/num2}")
print(f"{num1} * {num2} = {num1*num2}")
