"""Multiply number tho"""
num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
res = num1 * num2
print(f"{num1} x {num2} = {res}")

if res == 0:
    print('The result is positive and negative.')
elif res > 0:
    print("The result is positive.")
else:
    print("The result is negative.")
