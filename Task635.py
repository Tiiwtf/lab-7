# Create a function
def first_last(numbers):
    # Get the first and last numbers
    return [numbers[0], numbers[-1]]

# Enter numbers
numbers = list(map(int, input("Введіть числа: ").split()))

# Get the result
result = first_last(numbers)

# Print the result
print(result)