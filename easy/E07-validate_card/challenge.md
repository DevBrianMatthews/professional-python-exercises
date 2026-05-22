# E07 — Credit Card Validator

**Difficulty:** Easy  
**Topics:** Luhn algorithm, `str.isdecimal()`, list comprehensions, nested functions, type hints

---

## 🇬🇧 English

### Context

Credit card validation is a real-world data validation case used in any payment system. The Luhn algorithm is the industry standard used by Visa, Mastercard, and American Express to verify that a card number is potentially valid before sending it to the payment processor — catching typos before making expensive network calls.

### Task

Write a function `validate_card(card_number: str) -> tuple[bool, str]` that receives a card number as a string and returns:

- `True` if valid, `False` if not
- A descriptive message of the result

### Rules

1. The number must contain only digits — if it has letters or other characters, return `False`
2. It must have between 13 and 19 digits
3. It must pass the **Luhn algorithm**:
    - Traverse the digits from right to left
    - Digits at even positions (0, 2, 4...) are added as-is
    - Digits at odd positions (1, 3, 5...) are multiplied by 2 — if the result is greater than 9, subtract 9
    - If the total sum is a multiple of 10, the card is valid

### Expected output

```python
validate_card("4532015112830366")
# (True, "valid card number")

validate_card("1234567890123456")
# (False, "invalid card number")

validate_card("4532abc")
# (False, "card number must contain only digits")

validate_card("123")
# (False, "card number must be between 13 and 19 digits")
```

### Requirements

- Use type hints
- Descriptive messages in English for each case
- Implement the Luhn algorithm without external libraries
- Validations must run before the algorithm, in the correct order

---

## 🇪🇸 Español

### Contexto

La validación de tarjetas de crédito es un caso real de validación de datos en cualquier sistema de pagos. El algoritmo de Luhn es el estándar de la industria usado por Visa, Mastercard y American Express para verificar que un número de tarjeta es potencialmente válido antes de enviarlo al procesador de pagos — detectando errores tipográficos antes de hacer llamadas de red costosas.

### Tarea

Escribe una función `validate_card(card_number: str) -> tuple[bool, str]` que reciba un número de tarjeta como string y retorne:

- `True` si es válida, `False` si no
- Un mensaje descriptivo del resultado

### Reglas

1. El número debe contener solo dígitos — si tiene letras u otros caracteres, retorna `False`
2. Debe tener entre 13 y 19 dígitos
3. Debe pasar el **algoritmo de Luhn**:
    - Recorre los dígitos de derecha a izquierda
    - Los dígitos en posición par (0, 2, 4...) se agregan tal cual
    - Los dígitos en posición impar (1, 3, 5...) se multiplican por 2 — si el resultado es mayor a 9, se le resta 9
    - Si la suma total es múltiplo de 10, la tarjeta es válida

### Salida esperada

```python
validate_card("4532015112830366")
# (True, "valid card number")

validate_card("1234567890123456")
# (False, "invalid card number")

validate_card("4532abc")
# (False, "card number must contain only digits")

validate_card("123")
# (False, "card number must be between 13 and 19 digits")
```

### Requisitos

- Usa type hints
- Mensajes descriptivos en inglés para cada caso
- Implementa el algoritmo de Luhn sin librerías externas
- Las validaciones deben ejecutarse antes del algoritmo, en el orden correcto

---

## Submit your solution

Place your file at:

```
solutions/python/your_github_username.py
```

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full instructions.
