def reverse_alternate(st):
    st_list = st.split()
    result = []
    for index, word in enumerate(st_list):
        if index % 2 != 0:
            result.append(word[::-1])
        else:
            result.append(word)
    return " ".join(result)