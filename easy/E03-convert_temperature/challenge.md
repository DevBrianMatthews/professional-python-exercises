# E03 — Temperature Converter

**Difficulty:** Easy
**Topics:** `dict`, `lambda`, dispatch table, `ValueError`, type hints, input validation

---

## 🇬🇧 English

### Context

Conversion and transformation functions are everywhere in professional development — between units, formats, and data structures. This challenge also introduces a cleaner alternative to long `if/elif` chains: using a dictionary of functions (dispatch table) to handle multiple cases.

### Task

Write a function `conv_temp(value: float, from_unit: str, to_unit: str) -> float` that converts a temperature between `"celsius"`, `"fahrenheit"`, and `"kelvin"`.

### Validation rules

1. `from_unit` and `to_unit` must be one of the three valid units — otherwise raise `ValueError`
2. If `from_unit` and `to_unit` are the same, return the value as-is
3. A Kelvin value cannot be less than `0` — if it is, raise `ValueError`
4. Round the result to 2 decimal places

### Formulas

| From                | To         | Formula                                      |
| ------------------- | ---------- | -------------------------------------------- |
| Celsius             | Fahrenheit | `(value * 9/5) + 32`                         |
| Celsius             | Kelvin     | `value + 273.15`                             |
| Fahrenheit          | Celsius    | `(value - 32) * 5/9`                         |
| Kelvin              | Celsius    | `value - 273.15`                             |
| Fahrenheit ↔ Kelvin | —          | Convert through Celsius as intermediate step |

### Expected output

```python
conv_temp(100.0, "celsius", "fahrenheit")  # 212.0
conv_temp(0.0, "celsius", "kelvin")        # 273.15
conv_temp(98.6, "fahrenheit", "celsius")   # 37.0
conv_temp(-1.0, "kelvin", "celsius")       # ValueError
conv_temp(100.0, "celsius", "pluto")       # ValueError
```

### Requirements

- Use type hints
- Raise `ValueError` with descriptive messages in English
- No external libraries
- Do not use `if/elif` chains for the conversions — use a dispatch table instead

---

## 🇪🇸 Español

### Contexto

Las funciones de conversión y transformación aparecen en todo el desarrollo profesional — entre unidades, formatos y estructuras de datos. Este reto también introduce una alternativa más limpia a las cadenas largas de `if/elif`: usar un diccionario de funciones (dispatch table) para manejar múltiples casos.

### Tarea

Escribe una función `conv_temp(value: float, from_unit: str, to_unit: str) -> float` que convierta una temperatura entre `"celsius"`, `"fahrenheit"` y `"kelvin"`.

### Reglas de validación

1. `from_unit` y `to_unit` deben ser una de las tres unidades válidas — si no, lanza `ValueError`
2. Si `from_unit` y `to_unit` son iguales, retorna el mismo valor sin operar
3. Un valor en Kelvin no puede ser menor a `0` — si lo es, lanza `ValueError`
4. El resultado se redondea a 2 decimales

### Fórmulas

| De                  | A          | Fórmula                                          |
| ------------------- | ---------- | ------------------------------------------------ |
| Celsius             | Fahrenheit | `(value * 9/5) + 32`                             |
| Celsius             | Kelvin     | `value + 273.15`                                 |
| Fahrenheit          | Celsius    | `(value - 32) * 5/9`                             |
| Kelvin              | Celsius    | `value - 273.15`                                 |
| Fahrenheit ↔ Kelvin | —          | Convierte primero a Celsius como paso intermedio |

### Salida esperada

```python
conv_temp(100.0, "celsius", "fahrenheit")  # 212.0
conv_temp(0.0, "celsius", "kelvin")        # 273.15
conv_temp(98.6, "fahrenheit", "celsius")   # 37.0
conv_temp(-1.0, "kelvin", "celsius")       # ValueError
conv_temp(100.0, "celsius", "pluto")       # ValueError
```

### Requisitos

- Usa type hints
- Lanza `ValueError` con mensajes descriptivos en inglés
- Sin librerías externas
- No uses cadenas de `if/elif` para las conversiones — usa un dispatch table

---

## Submit your solution

Place your file at:

```
solutions/python/your_github_username.py
```

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full instructions.
