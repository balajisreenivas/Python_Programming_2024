
def has_greater_element(numbers,value):

    if not numbers:
        return False

    for num in numbers:
        if num > value:
            return True
    return False

numbers = [1,4,8,7,6,3,2]
value = 5

has_greater_element(numbers,value)



print(has_greater_element([10, 20, 30], 15))      # Output: True
print(has_greater_element([5, 7, 8], 10))        # Output: False
print(has_greater_element([], 5))                 # Output: False