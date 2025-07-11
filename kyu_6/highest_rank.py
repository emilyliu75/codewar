def highest_rank(arr):
    highest = 1
    num = arr[0]
    for item in arr:
        frequency = arr.count(item)
        if frequency >= highest:
            highest = frequency
            num = item
    a = [n for n in arr if arr.count(n) == highest]
    return max(a)