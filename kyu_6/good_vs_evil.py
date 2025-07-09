def good_vs_evil(good, evil):
    g = [1,2,3,3,4,10]
    b = [1,2,2,2,3,5, 10]
    good_score = 0
    evil_score = 0
    good = [int(i) for i in good.split()]
    evil = [int(i) for i in evil.split()]
    for i, v in enumerate(good):
        good_score += (v * g[i])
    for i, v in enumerate(evil):
        evil_score += (v * b[i])
    if good_score > evil_score:
        return "Battle Result: Good triumphs over Evil"
    elif good_score < evil_score:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"