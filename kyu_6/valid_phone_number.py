def valid_phone_number(phone_number):
    if len(phone_number) != 14:
        return False
    if phone_number[0] != "(" or phone_number[4] != ')' or phone_number[9] != "-":
        return False
    for item in "() -":
        if phone_number.count(item) > 1:
            return False
    return all(char in "() -" or char.isdigit() for char in phone_number)