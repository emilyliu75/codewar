def capitals(word):
    return [i for i, char in enumerate(word) if char.isupper()]
print(capitals("XsutqpbIFNpHoFaGLlhpGrbkZ"))

# should equal [0, 7, 8, 9, 11, 13, 15, 16, 20, 24])