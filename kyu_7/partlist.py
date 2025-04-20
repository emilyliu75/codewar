def partlist(arr):
    result = []
    for i,item in enumerate(arr):
        if 0 < i < len(arr):
            # print('first:', " ".join(arr[:i]))
            # print('second: ', " ".join(arr[i:]))
            # print("==============")
            tuple_set = (" ".join(arr[:i]), " ".join(arr[i:]))
            result.append(tuple_set)
    return result

print(partlist(["I", "wish", "I", "hadn't", "come"]))
print('\n[("I", "wish I hadn\'t come"), ("I wish", "I hadn\'t come"), ("I wish I", "hadn\'t come"), ("I wish I hadn\'t", "come")]')