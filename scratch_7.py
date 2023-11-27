def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        print (f"i ={i}")
        factorial = factorial * i
        print(f"factorial = {factorial}")
    return (factorial)


print(calculate_factorial(5))