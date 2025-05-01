def nb_dig(n, d):
    squares = [str(num * num) for num in range(n+1)]
    counts = 0
    for num in squares:
        counts += num.count(str(d))
    return counts

print(nb_dig(5750, 0))  # Expected output: 4700

