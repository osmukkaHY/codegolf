import string


def validate_username(uname: str) -> str:
    if not len(uname):
        return "Username cannot be empty."
    if len(uname) > 16:
        return "Username is too long."
    for char in uname:
        if char not in string.ascii_letters+string.digits+"_":
            return "Username can consist only of upper and lowercase ASCII letters, numbers and underscores."
    if uname[0] not in string.ascii_letters:
        return "Username must begin with an ASCII letter."

    return ""


def validate_passwords(pwd1: str, pwd2: str) -> str:
    if pwd1 != pwd2:
        return "Passwords don't match."
    if len(pwd1) < 4:
        return "Password must be at least 4 characters long."

    return ""
