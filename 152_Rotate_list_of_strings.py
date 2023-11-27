def rotate_strings(strings, n):
    if not strings or n == 0:  #Handle edge cases: if the list is empty or n is zero, return the original list.
        return strings
    for number in range(n):
        last_element = strings[-1] #Create a variable to hold the last element of the list.
        for i in range (len(strings)-1,0,-1): #Loop through the list from the end to the beginning, shifting each element one position to the right.
            strings[i] = strings[i-1]  #Assign the saved last element to the first position of the list.
        strings[0] = last_element
    return strings #Return the rotated list from the function


print(rotate_strings(['a', 'b', 'c'], 2))  # Output: ['b', 'c', 'a']
print(rotate_strings(['apple', 'banana', 'cherry', 'date'], 1))  # Output: ['date', 'apple', 'banana', 'cherry']
print(rotate_strings(['hello', 'world'], 3))  # Output: ['hello', 'world']
