def multiplication_table(size):
    result = []
    for i in range(1, size + 1):
        item = []
        for j in range(1, size + 1):
            item.append(j*i)
        result.append(item)

    return result