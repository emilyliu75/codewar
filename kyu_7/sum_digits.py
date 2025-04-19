def sum_digits(number):
    return sum(int(char) for char in str(abs(number)))