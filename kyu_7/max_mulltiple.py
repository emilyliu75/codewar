def max_multiple(divisor, bound):
    for i in range(bound, 1, -1):
        if i % divisor == 0:
            return i

# other solution
# def max_multiple(divisor, bound):
#     return bound - (bound % divisor)