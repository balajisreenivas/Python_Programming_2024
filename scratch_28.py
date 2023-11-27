def find_multiples(number,limit):
    multiples = []
    multiple = number
    while (multiple < limit):
        multiples.append(multiple)
        multiple += number
    return multiples

# Testing the function
print(find_multiples(3, 10))  # Expected Output: [3, 6, 9]