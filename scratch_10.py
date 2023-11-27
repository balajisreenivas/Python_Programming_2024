
#print("The quick brown fox jumps over the lazy dog".split())

import string
def find_longest_word(text):
    if (text == ''):
        return ''
    length_of_longest_word = 0
    longest_word = ''
    for word in text.split():
        if len(word) > length_of_longest_word:
            longest_word = word
            length_of_longest_word =len(word)
    return longest_word


print(find_longest_word("The quick brown fox jumps over the lazy dog"))

