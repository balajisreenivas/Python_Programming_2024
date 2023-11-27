def search_element(list_2D, target):
    for i in range (len(list_2D)):  # Gets the length of a 2D list
        for j in range (len(list_2D[i])): #Accessing the number of elements in each row
            if list_2D[i][j] == target:
                return (i,j)

    return (-1,-1)  # if




# Test the function
print(search_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5))  # Output: (1, 1)
print(search_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10))  # Output: (-1, -1)