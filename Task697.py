# Create a function
def print_reverse():
    # Enter a number
    n = int(input())

    # Stop if the number is 0
    if n == 0:
        print(n)
    else:
        # Call the function again
        print_reverse()

        # Print the number
        print(n)

# Ask the user to enter numbers
print("Введіть числа:")

# Start the function
print_reverse()