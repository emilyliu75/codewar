def fold_array(array, runs):
    def fold(array):
        mid_index = len(array) // 2
        o = []
        if len(array) % 2 != 0:
            for i,v in enumerate(array[:mid_index+1]):
                if i != mid_index:
                    new_value = array[i] + array[len(array)-1-i]
                    o.append(new_value)
                elif i == mid_index:
                    o.append(v)
        elif len(array) % 2 == 0:
            for i, v in enumerate(array[:mid_index]):
                new_value = array[i] + array[len(array) -1 - i]
                o.append(new_value)
        return o
    for i in range(1, runs+1):
        array = fold(array)
    return array
