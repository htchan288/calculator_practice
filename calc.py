# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

num1 = float(input("Enter frist number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")