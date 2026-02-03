# Task 1: Basic Mathematical Operations

# Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Division with error handling
if num2 != 0:
    division = num1 / num2
else:
    division = "Not possible (division by zero)"

# Display results
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
