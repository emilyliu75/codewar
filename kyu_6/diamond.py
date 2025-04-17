def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None
    half = n // 2 + 1
    output = ""
    for i in range(1, half):
        star_num = 2 * i -1
        space_num = int((n - star_num) / 2)
        line = " " * space_num + "*" * star_num
        output += f'{line}\n'

    output += ("*" * n + '\n')

    for i in range(half-1, 0, -1):
        star_num = 2 * i -1
        space_num = int((n - star_num) / 2)
        line = " " * space_num + "*" * star_num
        output += f'{line}\n'
    return output

print(diamond(3))
print(diamond(11))

# for i in range(1,3):
#     print(i)
# print(1//2)

