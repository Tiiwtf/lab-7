# Read numbers
def read_numbers():
    return list(map(int, input("Введіть числа: ").split()))

# Remove duplicate numbers
def remove_duplicates(numbers):
    return list(set(numbers))

# Get numbers
numbers = read_numbers()

# Remove duplicates
result = remove_duplicates(numbers)

# Print the result
print(result)