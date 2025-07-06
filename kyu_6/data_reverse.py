def data_reverse(data):
    bytes = []
    for i in range(0, len(data), 8):
        byte = data[i:i+8]
        bytes.append(byte)
    reversed = []
    for byte in bytes[::-1]:
        for item in byte:
            reversed.append(item)

    return reversed

# other solution
# def data_reverse(data):
#   res = []

#   for i in range(len(data)-8, -1, -8):
#     res.extend(data[i:i+8])

#   return res
