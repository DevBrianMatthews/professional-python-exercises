
def conv_temp(value: float, from_unit: str, to_unit: str) -> float:
    valid_units = {'celsius', 'fahrenheit', 'kelvin'}

    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError('The units must be written correctly.')

    if from_unit == 'kelvin' and value < 0:
        raise ValueError('Kelvin cannot be less than zero')

    if from_unit == to_unit:
        return value

    to_celsius = {
        'fahrenheit': lambda value: round((value - 32) * 5/9, 2),
        'kelvin':     lambda value: round(value - 273.15, 2),
        'celsius':    lambda value: value
    }

    from_celsius = {
        'fahrenheit': lambda value: round((value * 9/5) + 32, 2),
        'kelvin':     lambda value: round(value + 273.15, 2),
        'celsius':    lambda value: value
    }

    celsius_value = to_celsius[from_unit](value)
    return from_celsius[to_unit](celsius_value)

print(conv_temp(89.6, 'fahrenheit', 'celsius'))