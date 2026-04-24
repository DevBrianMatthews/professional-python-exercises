# E01 — Password Validator

**Difficulty:** Easy  
**Topics:** strings, `any()`, type hints, input validation

---

## 🇬🇧 English

### Context

Almost every system you build will need to validate user input. Password validation is one of the most common cases — and getting it wrong has real security consequences.

### Task

Write a function `validate_password(password: str) -> tuple[bool, list[str]]` that receives a password string and returns:

- `True` if the password is valid, `False` if not
- A list of the reasons it failed (empty if valid)

### Validation rules

1. Minimum 8 characters
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character from: `!@#$%^&*`

### Expected output

```python
validate_password("abc")
# (False, ["Mínimo 8 caracteres", "Falta mayúscula", "Falta dígito", "Falta carácter especial"])

validate_password("Abcdefg1!")
# (True, [])

validate_password("abcdefg1!")
# (False, ["Falta mayúscula"])
```

### Requirements

- Use type hints
- No external libraries — pure Python only
- Error messages should be clear and descriptive

---

## 🇪🇸 Español

### Contexto

Casi cualquier sistema que construyas va a necesitar validar el input del usuario. La validación de contraseñas es uno de los casos más comunes — y hacerlo mal tiene consecuencias reales de seguridad.

### Tarea

Escribe una función `validate_password(password: str) -> tuple[bool, list[str]]` que reciba una contraseña y retorne:

- `True` si es válida, `False` si no lo es
- Una lista con los motivos de fallo (vacía si es válida)

### Reglas de validación

1. Mínimo 8 caracteres
2. Al menos una letra mayúscula
3. Al menos una letra minúscula
4. Al menos un dígito
5. Al menos uno de estos caracteres especiales: `!@#$%^&*`

### Salida esperada

```python
validate_password("abc")
# (False, ["Mínimo 8 caracteres", "Falta mayúscula", "Falta dígito", "Falta carácter especial"])

validate_password("Abcdefg1!")
# (True, [])

validate_password("abcdefg1!")
# (False, ["Falta mayúscula"])
```

### Requisitos

- Usa type hints
- Sin librerías externas — solo Python puro
- Los mensajes de error deben ser claros y descriptivos

---

## Submit your solution

Place your file at:
```
solutions/python/your_github_username.py
```

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full instructions.
