import sys

def add(x, y):
    """Returns the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Returns the difference of two numbers."""
    return x - y

def multiply(x, y):
    """Returns the product of two numbers."""
    return x * y

def divide(x, y):
    """
    Returns the quotient of two numbers.
    Raises ZeroDivisionError if the divisor (y) is zero.
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def display_menu():
    """Prints the available operations to the console."""
    print("\n--- Simple Python CLI Calculator ---")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("-" * 34)

def get_numeric_input(prompt):
    """
    Prompts the user for input and ensures the input can be converted to a float.

    Args:
        prompt (str): The text to display to the user.

    Returns:
        float: The successfully converted numeric input.
    """
    while True:
        try:
            # Read user input and attempt to convert it to a float
            value = float(input(prompt))
            return value
        except ValueError:
            # Handle case where input is not a valid number
            print("Invalid input. Please enter a valid number.")

def run_calculator():
    """Main loop for the command-line calculator."""
    while True:
        display_menu()

        # Get the user's operation choice
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            sys.exit(0)
        
        # Validate operation choice
        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        # Get the two numbers for the calculation
        num1 = get_numeric_input("Enter first number: ")
        num2 = get_numeric_input("Enter second number: ")

        result = None
        operation_symbol = ""

        # Perform the chosen operation, handling calculation-specific errors
        try:
            if choice == '1':
                result = add(num1, num2)
                operation_symbol = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation_symbol = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation_symbol = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation_symbol = "/"

            # Display the result
            print(f"\nResult: {num1} {operation_symbol} {num2} = {result}")

        except ZeroDivisionError as e:
            print(f"\nCalculation Error: {e}")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"\nAn unexpected error occurred: {e}")


# Start the application
if __name__ == "__main__":
    run_calculator()
