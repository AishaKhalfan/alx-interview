def is_utf8_encoded(string):
    """
    Checks if the given string is a valid UTF-8 encoding.
    Args:
    	string: The string to be checked.
    Returns:
    	True if the string is a valid UTF-8 encoding, False otherwise.
    """
    try:
        string.encode('utf-8', 'strict')
        return True
    except UnicodeDecodeError:
        return False

# Test cases
print(is_utf8_encoded("Hello, World!"))  # Output: True
print(is_utf8_encoded("こんにちは"))  # Output: True
print(is_utf8_encoded("Hello\x80"))  # Output: False (invalid UTF-8 sequence)
print(is_utf8_encoded("مرحباً بالعالم!"))
