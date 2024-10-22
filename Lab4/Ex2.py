#Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string and the values are the number of occurrences of that character in the given text. Example: For string "Ana has apples." given as a parameter the function will return the dictionary:

#{'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .
def count_characters(string):
    char_count = {}
    for c in string:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count
text = "Ana has apples."
result = count_characters(text)
print(result)