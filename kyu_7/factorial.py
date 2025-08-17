def factorial(n):
    if n <= 1:
        return 1
    result = n
    while n != 1:
        n -= 1
        result *= n
    return result

print(factorial(0))  #