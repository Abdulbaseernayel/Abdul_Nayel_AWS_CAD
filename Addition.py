# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Main program
if __name__ == "__main__":
    # Input two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Add the numbers
    result = add_numbers(num1, num2)

    # Print the result
    print("The sum of", num1, "and", num2, "is:", result)
