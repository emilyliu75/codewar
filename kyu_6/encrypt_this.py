def encrypt_this(text):
    def convert(t):
        if len(t) == 0:
            return ""
        elif len(t) == 1:
            return str(ord(t))
        elif len(t) == 2:
            return str(ord(t[0])) + t[1]
        else:
            result = str(ord(t[0])) + t[-1]
            for i in range(2, len(t) -1):
                result += t[i]
            result += t[1]
        return result
    if " " not in text:
        return convert(text)
    else:
        text_in_list = text.split()
        convert_list = [convert(t) for t in text_in_list]
        return " ".join(convert_list)


print(encrypt_this('Hello'))
print(encrypt_this("A wise old owl lived in an oak"))