# Version 1 - Basic Implementation

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    return num1 / num2

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division")
choice = input("Enter choice: ")

if choice == '1':
    print("Result:", add_numbers(num1, num2))
elif choice == '2':
    print("Result:", subtract_numbers(num1, num2))
elif choice == '3':
    print("Result:", multiply_numbers(num1, num2))
elif choice == '4':
    print("Result:", divide_numbers(num1, num2))
    