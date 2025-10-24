def validate(n):
    initial_list = [int(num) for num in str(n)]
    new_list = []
    if len(initial_list) % 2 == 0:
        for i,v in enumerate(initial_list):
            if i % 2 == 0:
                if v*2 > 9:
                    new_list.append(v*2 - 9)
                else:
                    new_list.append(v*2)
            else:
                new_list.append(v)
    else:
        for i,v in enumerate(initial_list):
            if i % 2 != 0:
                if v*2 > 9:
                    new_list.append(v*2 - 9)
                else:
                    new_list.append(v*2)
            else:
                new_list.append(v)
    if sum(new_list) % 10 == 0:
        return True
    return False
