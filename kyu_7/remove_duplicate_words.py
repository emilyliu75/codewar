def remove_duplicate_words(s):
    removed =[]
    w = s.split()
    for word in w:
        if word not in removed:
            removed.append(word)
    return " ".join(removed)

print(remove_duplicate_words("my cat is my cat fat"), "\nmy cat is fat")