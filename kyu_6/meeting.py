def meeting(s):
    s = s.upper()
    names = s.split(";")
    upper_names = [(n.split(":")[1], n.split(":")[0]) for n in names]
    res = sorted(upper_names, key=lambda x:(x[0], x[1]))
    return "".join("(%s, %s)" % tup for tup in res)
    # return "".join(f"({l}, {f})" for l,f in res)

# other solution
# def meeting(s):
#     return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))