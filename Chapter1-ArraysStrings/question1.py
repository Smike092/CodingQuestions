def has_unique_characters(string):
    # Sort the string
    sorted_string = sorted(string)
    
    # Iterate through the string to check consecutive characters
    for i in range(len(sorted_string) - 1):
        # If two consecutive characters are the same, the string doesn't have unique characters
        if sorted_string[i] == sorted_string[i + 1]:
            return False
    
    # If no characters are the same, the string has unique characters
    return True

# Example usage
string1 = "abcdefg"
string2 = "hello"
print(has_unique_characters(string1))  # Output: True
print(has_unique_characters(string2))  # Output: False
