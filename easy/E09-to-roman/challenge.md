# E09 — Roman Number Converter

**Difficulty:** Easy  
**Topics:** `dict`, `reversed()`, nested loops, type hints, mapping tables

---

## 🇬🇧 English

### Context

Converters and parsers are common tasks in professional development — reading data from external sources, transforming between representations, and validating formats. This challenge reinforces using dictionaries as mapping tables and algorithmic thinking over sequences.

### Task

Write a function `to_roman(number: int) -> str` that converts an integer to its Roman numeral representation.

### Rules

1. `number` must be an integer between `1` and `3999` — otherwise raise `ValueError`
2. Use the standard value table including subtraction cases:

| Value | Symbol |
| ----- | ------ |
| 1000  | M      |
| 900   | CM     |
| 500   | D      |
| 400   | CD     |
| 100   | C      |
| 90    | XC     |
| 50    | L      |
| 40    | XL     |
| 10    | X      |
| 9     | IX     |
| 5     | V      |
| 4     | IV     |
| 1     | I      |

### Expected output

```python
to_roman(1)     # "I"
to_roman(4)     # "IV"
to_roman(9)     # "IX"
to_roman(58)    # "LVIII"
to_roman(1994)  # "MCMXCIV"
to_roman(3999)  # "MMMCMXCIX"
to_roman(0)     # ValueError: number must be between 1 and 3999
to_roman(4000)  # ValueError: number must be between 1 and 3999
```

### Requirements

- Use type hints
- Raise `ValueError` with a descriptive message in English
- Use the value table as a data structure, not as `if/elif` chains
- The algorithm must work for any number in the valid range

---

## 🇪🇸 Español

### Contexto

Los conversores y parsers son tareas comunes en el desarrollo profesional — leer datos de fuentes externas, transformar entre representaciones y validar formatos. Este reto refuerza el uso de diccionarios como tablas de mapeo y el pensamiento algorítmico sobre secuencias.

### Tarea

Escribe una función `to_roman(number: int) -> str` que convierta un número entero a su representación en números romanos.

### Reglas

1. `number` debe ser un entero entre `1` y `3999` — si no, lanza `ValueError`
2. Usa la tabla de valores estándar incluyendo los casos de sustracción:

| Valor | Símbolo |
| ----- | ------- |
| 1000  | M       |
| 900   | CM      |
| 500   | D       |
| 400   | CD      |
| 100   | C       |
| 90    | XC      |
| 50    | L       |
| 40    | XL      |
| 10    | X       |
| 9     | IX      |
| 5     | V       |
| 4     | IV      |
| 1     | I       |

### Salida esperada

```python
to_roman(1)     # "I"
to_roman(4)     # "IV"
to_roman(9)     # "IX"
to_roman(58)    # "LVIII"
to_roman(1994)  # "MCMXCIV"
to_roman(3999)  # "MMMCMXCIX"
to_roman(0)     # ValueError: number must be between 1 and 3999
to_roman(4000)  # ValueError: number must be between 1 and 3999
```

### Requisitos

- Usa type hints
- Lanza `ValueError` con mensaje descriptivo en inglés
- Usa la tabla de valores como estructura de datos, no como cadenas de `if/elif`
- El algoritmo debe funcionar para cualquier número en el rango válido

---

## Submit your solution

Place your file at:

```
solutions/python/your_github_username.py
```

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full instructions.
