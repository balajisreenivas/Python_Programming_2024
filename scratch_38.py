def encode_strings(strings):

    encoded_list = []

    for string in strings:
        encoded_string = ''
        # Encoding
        for char in string:
            if char == 'z':
                encoded_char = 'a'
            elif char == 'Z':
                encoded_char = 'A'
            else:
                encoded_char = chr(ord(char) + 1)

            encoded_string = encoded_string + encoded_char

        encoded_list.append(encoded_string)
    return encoded_list



print(encode_strings(['abc', 'def']))  # Output: ['bcd', 'efg']
print(encode_strings(['hello', 'WORLD']))  # Output: ['ifmmp', 'XPSME']
print(encode_strings(['zoo']))  # Output: ['app']
print(encode_strings(['']))  # Output: ['']