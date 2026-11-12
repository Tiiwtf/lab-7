# Create a function
def sort_by_length_desc(text):
    # Split text into words
    words = text.split()

    # Sort words by length in descending order
    return " ".join(sorted(words, key=lambda word: (-len(word), word)))

# Enter words
text = input("Введіть слова: ")

# Get the result
result = sort_by_length_desc(text)

# Print the result
print(result)