def clean_string(s):
    output = ''
    for char in s:
        if char != '#':
            output += char
        elif char == "#" and len(output) != 0:
            output = output[:-1]
    return output

# should be 'ac'
print(clean_string('abc#d##c'))

# test...writing this in main branch
# git stash           # Temporarily saves your changes
# git checkout -b new-branch-name
# git stash pop       # Applies your changes on the new branch
