# E04 — Password Generator

**Difficulty:** Easy  
**Topics:** `random`, `string`, `random.choice()`, `random.shuffle()`, parameters with defaults, type hints

---

## en English

### Context

Generating random strings is a common task in professional development — tokens, temporary IDs, verification codes, and passwords all follow the same pattern. This challenge introduces the `random` and `string` modules, and the concept of building a pool of characters to draw from.

### Task

Write a function `generate_password(length: int = 12, uppercase: bool = True, digits: bool = True, special_chars: bool = True) -> str` that generates a random password.

### Rules

1. `length` must be at least `8` — otherwise raise `ValueError`
2. At least one character type must be active — if all three booleans are `False`, raise `ValueError`
3. The password must **guaranteed** contain at least one character of each active type — it must be enforced, not just possible
4. Valid special characters: `!@#$%^&*`
5. Lowercase letters are always included

### Expected output

```python
generate_password()
# 'aB3!xkR9@mQz'  (12 chars, all types active)

generate_password(length=8, uppercase=False, special_chars=False)
# 'a3kx9mq2'  (lowercase and digits only)

generate_password(length=6)
# ValueError: length must be at least 8

generate_password(length=8, uppercase=False, digits=False, special_chars=False)
# ValueError: at least one character type must be enabled
```

### Requirements

- Use type hints
- Parameters must have default values
- Raise `ValueError` with descriptive messages in English
- Use `random.choice()` and `random.shuffle()`
- Use the `string` module instead of hardcoded character lists

---

## 🇪🇸 Español

### Contexto

Generar strings aleatorios es una tarea común en el desarrollo profesional — tokens, IDs temporales, códigos de verificación y contraseñas siguen el mismo patrón. Este reto introduce los módulos `random` y `string`, y el concepto de construir un pool de caracteres del cual tomar elementos aleatorios.

### Tarea

Escribe una función `generate_password(length: int = 12, uppercase: bool = True, digits: bool = True, special_chars: bool = True) -> str` que genere una contraseña aleatoria.

### Reglas

1. `length` debe ser mínimo `8` — si no, lanza `ValueError`
2. Al menos un tipo de carácter debe estar activo — si los tres booleanos son `False`, lanza `ValueError`
3. La contraseña debe contener **garantizadamente** al menos un carácter de cada tipo activado — debe ser obligatorio, no solo posible
4. Caracteres especiales válidos: `!@#$%^&*`
5. Las letras minúsculas siempre están incluidas

### Salida esperada

```python
generate_password()
# 'aB3!xkR9@mQz'  (12 chars, todos los tipos activos)

generate_password(length=8, uppercase=False, special_chars=False)
# 'a3kx9mq2'  (solo minúsculas y dígitos)

generate_password(length=6)
# ValueError: length must be at least 8

generate_password(length=8, uppercase=False, digits=False, special_chars=False)
# ValueError: at least one character type must be enabled
```

### Requisitos

- Usa type hints
- Los parámetros deben tener valores por defecto
- Lanza `ValueError` con mensajes descriptivos en inglés
- Usa `random.choice()` y `random.shuffle()`
- Usa el módulo `string` en vez de listas de caracteres escritas a mano

---

## Submit your solution

Place your file at:

```
solutions/python/your_github_username.py
```

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full instructions.
