def encode(st):
    st = st.replace('a', '1').replace('e','2').replace('i', '3').replace('o', '4').replace('u', '5')
    return st

def decode(st):
    st = st.replace('1', 'a').replace('2', 'e').replace('3', 'i').replace('4','o').replace('5', 'u')
    return st


# other solutions
CIPHER = ("aeiou", "12345")

def encode(st):
    return st.translate(str.maketrans(CIPHER[0], CIPHER[1]))

def decode(st):
    return  st.translate(str.maketrans(CIPHER[1], CIPHER[0]))