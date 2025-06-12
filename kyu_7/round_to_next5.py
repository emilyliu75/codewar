def round_to_next5(n):
    if n % 5 == 0:
        return n
    return (n // 5 + 1) * 5

print(round_to_next5(0))  # 0
print(round_to_next5(2))  # 5
print(round_to_next5(5))  # 5
print(round_to_next5(-1)) # 0