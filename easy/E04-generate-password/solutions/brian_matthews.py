import random
import string

def generate_password(length: int = 12, uppercase: bool = True, digits: bool = True, special_chars: bool = True) -> str:
    lowercase   = string.ascii_lowercase
    upper       = string.ascii_uppercase
    nums        = string.digits
    simbols     = '!@#$%^&*'

    password = []
    pool     = lowercase

    if length < 8:
        raise ValueError('length must be at least 8')

    if not uppercase and not digits and not special_chars:
        raise ValueError('at least one character type must be enabled.')

    if uppercase:
        password.append(random.choice(upper))
        pool += upper

    if digits:
        password.append(random.choice(nums))
        pool += nums

    if special_chars:
        password.append(random.choice(simbols))
        pool += simbols

    while length > len(password):
        password.append(random.choice(pool))

    random.shuffle(password)
    text = ''.join(password)

    return text

print(generate_password())