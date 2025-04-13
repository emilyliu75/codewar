def rev_rot(strng, sz):
    if sz <= 0 or sz >= len(strng) or not strng:
        return ""
    parts = [strng[i:i+sz] for i in range(0, len(strng), sz)]
    print(parts)
    result = ''
    for part in parts:
        print('current part', part)
        if len(part) == sz:
            if sum(int(p) for p in part) % 2 == 0:
                part = part[::-1]
                result += part
            else:
                part = part[1:] + part[0]
                result += part
    return result


s = "733049910872815764"
print(rev_rot(s, 5), "\n330479108928157")

