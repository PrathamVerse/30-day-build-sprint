# Day 1 - Python Basics

# 1. Ask user's name, print "Hello [name]!"
name = input("What's your name? ")
print(f"Hello {name}!")

# 2. Ask two numbers, print their sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Sum: {num1 + num2}")

# 3. Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")