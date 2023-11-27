import string

def is_hex_string (string):

    if not string:
        return False

    hex_digits = '0123456789abcdefABCDEF'

    for ch in string:
        if ch not in hex_digits:
            return False
    return True



print(is_hex_string('1a2f4C'))  # Output: True
print(is_hex_string('1g2f4C'))  # Output: False
print(is_hex_string(''))  # Output: False