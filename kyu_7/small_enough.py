def small_enough(array, limit):
    for i in array:
        if i > limit:
            return False
    return True

# other solution
# def small_enough(array, limit):
#     return all(i <= limit for i in array)
