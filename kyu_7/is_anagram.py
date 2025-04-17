# write the function is_anagram
def is_anagram(test, original):
    if len(test) != len(original):
        return False
    for char in test.lower():
        if char not in original.lower():
            return False
        elif test.lower().count(char) != original.lower().count(char):
            return False
    return True

# other solutions
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())