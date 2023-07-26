def is_valid_utf8(encoded_string):
    try:
        decoded_string = encoded_string.decode('utf-8')
    except UnicodeDecodeError:
        return False
    return True

valid_string = b'Hello, this is a valid UTF-8 string!'
invalid_string = b'\xff\xfe\xfd'  # Invalid UTF-8 characters

print(is_valid_utf8(valid_string))   # Output: True
print(is_valid_utf8(invalid_string)) # Output: False
