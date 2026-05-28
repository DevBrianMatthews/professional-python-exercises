
def to_roman(number: int) -> str:

    if not 1 <= number <= 3999:
        raise ValueError('number must be between 1 and 3999')

    num_roman = {
        'I':    1,
        'IV':   4,
        'V':    5,
        'IX':   9,
        'X':    10,
        'XL':   40,
        'L':    50,
        'XC':   90,
        'C':    100,
        'CD':   400,
        'D':    500,
        'CM':   900,
        'M':    1000
    }
    roman = []
    num   = number

    for key, value in reversed(num_roman.items()):
        while value <= num:
            roman.append(key)
            num -= value

    return ''.join(roman)


print(to_roman(0))
