def reverse_letter(st):
    output = ''
    for item in st:
        if item.isalpha():
            output += item
    return output[::-1]

# other solution
# def reverse_letter(s):
#   return ''.join([i for i in s if i.isalpha()])[::-1]