# Create a function
def power(a, b):
    # Stop when b is 0
    if b == 0:
        return 1

    # Multiply a by the result of the function
    return a * power(a, b - 1)

# Enter a and b
a, b = map(int, input("Введіть a і b: ").split())

# Calculate the power
result = power(a, b)

# Print the result
print(result)