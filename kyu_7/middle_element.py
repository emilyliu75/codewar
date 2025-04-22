def gimme(input_array):
    for num in input_array:
        if num != min(input_array) and num != max(input_array):
            return input_array.index(num)