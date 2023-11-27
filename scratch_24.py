def are_sums_equal(list1,list2):
    if not list1 or not list2: #checks if list1 or list2 is EMPTY
        return False

    sum1 = 0

    for value in list1:

        sum1 += value

    sum2 = 0

    for value in list2:

        sum2 += value

    return sum1 == sum2



print(are_sums_equal([10, 20, 30], [15, 25, 20]))  # Output: True
print(are_sums_equal([5, 10, 15], [5, 10, 14]))  # Output: False
print(are_sums_equal([1, 2, 3, 4], [4, 3, 2, 1]))  # Output: True
print(are_sums_equal([], [4, 3, -7]))  # Output: False
print(are_sums_equal([1, 2], []))  # Output: False