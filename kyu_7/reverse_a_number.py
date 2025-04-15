def reverse_number(n):
    if n > 0:
        return int(str(n)[::-1])
    else:
        return int(str(n*-1)[::-1]) * -1

print(reverse_number(123), "\n321")

print(reverse_number(-123), "\n-321")