def solve(s):
    lower_letters = [i for i in s if i.lower() == i]
    upper_letters = [i for i in s if i.upper() == i]
    if len(lower_letters) >= len(upper_letters):
        return s.lower()
    else:
        return s.upper()