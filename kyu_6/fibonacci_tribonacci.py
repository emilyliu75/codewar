def xbonacci(signature, n):
    length = len(signature)
    if length == n:
        return signature
    elif n > length:
        shortage = n - length
        print(shortage)
        for i in range(shortage):
            print("appending: ", signature[(len(signature)-i)*(-1):])
            print('shortage', i)
            print("length", len(signature))
            signature.append(sum(signature[(len(signature)-i)*(-1):]))
    return signature[:n]


test1 = [0,1]
print(xbonacci(test1, 10))
print([0,1,1,2,3,5,8,13,21,34])

# print("-----------")
test2=[0,0,0,0,1]
print(xbonacci(test2, 10))
print([0,0,0,0,1,1,2,4,8,16])
# print(sum([1,2,3,0,0][-2:]))