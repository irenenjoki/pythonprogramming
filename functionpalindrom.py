def is_palindrome(string):
    # Remove any whitespace and convert the string to lowercase
    string = string.replace(" ", "").lower()
    
    # Reverse the string
    reversed_string = string[::-1]
    
    # Check if the original string and the reversed string are equal
    if string == reversed_string:
        return True
    else:
        return False
print(is_palindrome("radar"))  # True
print(is_palindrome("Hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True
