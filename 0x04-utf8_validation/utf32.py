decimal_value = 127998

# Convert decimal to binary
binary_value = bin(decimal_value)

print(f"Binary representation of {decimal_value}: {binary_value}")

# Unicode code point for 😶 (Face Without Mouth emoji)
unicode_code_point = 0x1F636

# Use chr() to get the Unicode character from the code point
unicode_character = chr(unicode_code_point)

# Encode the Unicode character in UTF-32
utf32_encoded = unicode_character.encode('utf-32')

# Convert the bytes to binary representation
utf32_binary = ''.join(format(byte, '08b') for byte in utf32_encoded)

print(f"UTF-32 encoded value for U+1F636 (😶) in binary: {utf32_binary}")

