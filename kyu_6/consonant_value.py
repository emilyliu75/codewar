def solve(s):
    change = ('aeiou', ',,,,,')
    new = s.translate(str.maketrans(change[0], change[1]))
    consonant = new.split(",")
    highest = 0
    for item in consonant:
        if item != '':
            score = 0
            for i in item:
                score += (ord(i) - 96)
                highest = max(score, highest)
    return highest

