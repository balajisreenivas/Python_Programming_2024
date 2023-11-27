#5, 15 , 25 , 35
#s             e

def reverse_list(list):
    start = 0
    end = len(list) - 1

    while(start<end):
        print(f"start = {start}")
        print(list)
        list[start], list[end] = list[end] , list[start]
        start +=1
        end -=1
        print(f"end = {end}")

    return list


# Testing the function with examples
print(reverse_list([10, 20, 30,40,50]))      # Output: [30, 20, 10]
