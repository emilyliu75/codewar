def min_value(digits):
    remove_dup = [str(n) for n in sorted(list(set(digits)))]
    return int("".join(remove_dup))

# other solution
# def min_value(digits):
#      return int("".join(map(str,sorted(set(digits)))))