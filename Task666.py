# Create a function
def sort_by_length(text):
    # Split text into words
    words = text.split()

    # Sort words by length and alphabetically
    return " ".join(sorted(words, key=lambda word: (len(word), word)))

# Enter words
text = input("Введіть слова: ")

# Get the result
result = sort_by_length(text)

# Print the result
print(result)