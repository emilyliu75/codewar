def up_array(arr):
    if not arr or any(n<0 or n>9 for n in arr):
        return None
    arr_str = [str(n) for n in arr]
    number = int("".join(arr_str)) + 1
    str_number = "".join(str(number))
    result = [int(n) for n in str_number]
    if len(result) == len(arr):
        return result
    else:
        missing_0 = len(arr) - len(result)
        return [0] * missing_0 + result

print(up_array([0,4,2]))
print(up_array([9,9]))