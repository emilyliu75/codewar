def race(v1, v2, g):
    if v2 <=v1:
        return None
    time_to_catch = g/(v2-v1) * 3600
    # print(time_to_catch)
    hour = time_to_catch //3600
    minute = time_to_catch // 60 % 60
    second = time_to_catch % 60

    return [int(hour), int(minute), int(second)]


# print(race(720, 850, 70), '\n[0, 32, 18]')
print(race(820, 850, 550), '\n[18, 20, 0]')