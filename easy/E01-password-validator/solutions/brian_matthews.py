
def validate_password(password: str) -> tuple[bool, list[str]]:
    simbols = '!@#$%^&*'
    errors = []

    if not any(x.isupper() for x in password):
        errors.append('Faltan mayúsculas')

    if not any(x.islower() for x in password):
        errors.append('Faltan minúsculas')

    if not any(x in simbols for x in password):
        errors.append('Faltan símbolos')

    if not any(x.isdigit() for x in password):
        errors.append('Faltan números')

    if len(password) < 8:
        errors.append('Mínimo 8 caracteres')

    return (not errors, errors)

print(validate_password('abc595'))