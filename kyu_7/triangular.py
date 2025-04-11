def triangular(n):
    # passed but too slow
    # if n <= 0:
    #     return 0
    # result = 0
    # for i in range(1, n+1):
    #     result += i
    # return result
    if n <= 0:
        return 0
    return n * (n+1) // 2