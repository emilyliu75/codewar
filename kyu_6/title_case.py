def title_case(title, minor_words=''):
    if not minor_words:
        return title.title()
    minor_list = [w.lower() for w in minor_words.split()]
    title_list = title.split()
    output = []
    output.append(title_list[0].title())
    for word in title_list[1:]:
        if word.lower() in minor_list:
            output.append(word.lower())
        else:
            output.append(word.title())
    print(title, minor_words)
    return " ".join(output)
