def check_exam(arr1,arr2):
    result = 0
    for i in range(len(arr1)):
        if arr2[i] == "":
            result += 0
        elif arr1[i] == arr2[i]:
            result += 4
        else:
            result -= 1
    return max(result, 0)

# other solution
# def check_exam(arr1, arr2):
#     return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))