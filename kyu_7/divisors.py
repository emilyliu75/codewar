def divisors(n):
    output = []
    for i in range(1, n+1):
        if (n / i).is_integer():
            output.append(i)
    return len(output)