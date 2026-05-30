
def calculate_bmi(weight: float, height: float, unit: str = "metric") -> dict:

    if weight <= 0:
        raise ValueError('weight must be greater than 0')
    if height <= 0:
        raise ValueError('height must be greater than 0')

    if unit not in ('imperial', 'metric'):
        raise ValueError('unit must be metric or imperial')

    unit_table = {
        'metric'  : lambda: round((weight / height ** 2), 2),
        'imperial': lambda: round((703 * weight / height ** 2), 2)
    }

    result = unit_table[unit]()

    categories = [
        (18.5, 'Underweight'),
        (25.0, 'Normal weight'),
        (30.0, 'Overweight'),
    ]

    for value, label in categories:
        if result < value:
            return {'bmi': result, 'category': label, 'unit': unit }
    return {'bmi': result, 'category': 'Obesity', 'unit': unit }

print(calculate_bmi(80.5, 1.85))