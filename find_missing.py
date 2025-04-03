# 6 kyu
def find_missing(sequence):
    diffs = []
    length = len(sequence)
    for i in range(length):
        if i < length - 1:
            diff = sequence[i+1] - sequence[i]
            diffs.append(diff)
    # print(diffs)
    freq = {}
    for d in diffs:
        freq[d] = freq.get(d, 0) + 1
    # print(freq)
    common_diff = max(freq, key=freq.get)
    # print(common_diff)
    for i in range(length-1):
        if sequence[i] + common_diff != sequence[i+1]:
            return sequence[i] + common_diff

print("should be: 5")
print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))
# print("\n")
# print("should be: 2")
# print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))

print("\n")
print("should be: -21")
print(find_missing( [-3, -9, -15, -27, -33, -39, -45, -51, -57]))


print("\n")
print("should be: -406")
print(find_missing([-22, -70, -118, -166, -214, -262, -310, -358, -454]))

print("\n")
print("should be: 114")
print(find_missing([-30, -12, 6, 24, 42, 60, 78, 96, 132]))