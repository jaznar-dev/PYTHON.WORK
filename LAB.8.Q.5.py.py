import string


def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in string.punctuation for c in password):
        return False

    return True



print(is_valid_password("Password123!"))
print(is_valid_password("weakpass"))
print(is_valid_password("Short1!"))