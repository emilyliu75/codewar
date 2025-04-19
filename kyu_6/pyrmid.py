def pyramid(n):
    result = []
    for i in range(1, n+1):
        item = [1 for j in range(i)]
        result.append(item)
    return result

print(pyramid(0), '\n[]')
print(pyramid(1), '\n[[1]]')
print(pyramid(2), '\n[[1], [1, 1]]')