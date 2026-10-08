# Version 2 

def add_numbers(num1, num2):
    """Calculates and returns the sum of two numbers."""
    return num1 + num2

def subtract_numbers(num1, num2):
    """Calculates and returns the difference of two numbers."""
    return num1 - num2

def multiply_numbers(num1, num2):
    """Calculates and returns the product of two numbers."""
    return num1 * num2

def divide_numbers(num1, num2):
    """Calculates and returns the quotient, handling division by zero safely."""
    if num2 == 0:
        return "Cannot divide by zero."
    return num1 / num2

def main():
    print("-Modular Calculator Mini-Program-")
    
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    choice = input("\nEnter choice (1-4): ")

    if choice == '1':
        result = add_numbers(first_num, second_num)
    elif choice == '2':
        result = subtract_numbers(first_num, second_num)
    elif choice == '3':
        result = multiply_numbers(first_num, second_num)
    elif choice == '4':
        result = divide_numbers(first_num, second_num)
    else:
        result = "Invalid choice selected."

    #final result
    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()