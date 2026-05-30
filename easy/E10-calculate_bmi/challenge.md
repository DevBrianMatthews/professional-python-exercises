# E10 — BMI Calculator

**Difficulty:** Easy  
**Topics:** `dict`, `lambda`, dispatch table, range matching, type hints, default parameters

---

## 🇬🇧 English

### Context

Health metric calculators appear in medical, fitness, and insurance apps. This challenge closes the `easy` block by combining a dispatch table for unit systems with a range-matching pattern for categories — two patterns that appear constantly in professional backends.

### Task

Write a function `calculate_bmi(weight: float, height: float, unit: str = "metric") -> dict` that calculates the BMI and returns:

- `bmi` — BMI value rounded to 2 decimal places
- `category` — category according to the standard WHO table
- `unit` — unit system used

### WHO Categories

| BMI         | Category      |
| ----------- | ------------- |
| < 18.5      | Underweight   |
| 18.5 – 24.9 | Normal weight |
| 25.0 – 29.9 | Overweight    |
| ≥ 30.0      | Obesity       |

### Unit systems

- `"metric"` — weight in kg, height in meters. Formula: `weight / height ** 2`
- `"imperial"` — weight in pounds, height in inches. Formula: `703 * weight / height ** 2`

### Rules

1. `weight` must be greater than `0` — otherwise raise `ValueError`
2. `height` must be greater than `0` — otherwise raise `ValueError`
3. `unit` must be `"metric"` or `"imperial"` — otherwise raise `ValueError`

### Expected output

```python
calculate_bmi(70, 1.75)
# {"bmi": 22.86, "category": "Normal weight", "unit": "metric"}

calculate_bmi(154, 69, unit="imperial")
# {"bmi": 22.74, "category": "Normal weight", "unit": "imperial"}

calculate_bmi(-70, 1.75)
# ValueError: weight must be greater than 0

calculate_bmi(70, 1.75, unit="random")
# ValueError: unit must be metric or imperial
```

### Requirements

- Use type hints with an optional parameter
- Raise `ValueError` with descriptive messages in English
- Use a dispatch table for unit systems
- Use a list of tuples for category ranges — no `if/elif` chains for categories

---

## 🇪🇸 Español

### Contexto

Las calculadoras de métricas de salud aparecen en apps médicas, de fitness y de seguros. Este reto cierra el bloque `easy` combinando un dispatch table para sistemas de unidades con un patrón de rangos para categorías — dos patrones que aparecen constantemente en backends profesionales.

### Tarea

Escribe una función `calculate_bmi(weight: float, height: float, unit: str = "metric") -> dict` que calcule el IMC y retorne:

- `bmi` — valor del IMC redondeado a 2 decimales
- `category` — categoría según la tabla estándar de la OMS
- `unit` — sistema de unidades usado

### Categorías OMS

| IMC         | Categoría     |
| ----------- | ------------- |
| < 18.5      | Underweight   |
| 18.5 – 24.9 | Normal weight |
| 25.0 – 29.9 | Overweight    |
| ≥ 30.0      | Obesity       |

### Sistemas de unidades

- `"metric"` — peso en kg, altura en metros. Fórmula: `weight / height ** 2`
- `"imperial"` — peso en libras, altura en pulgadas. Fórmula: `703 * weight / height ** 2`

### Reglas

1. `weight` debe ser mayor a `0` — si no, lanza `ValueError`
2. `height` debe ser mayor a `0` — si no, lanza `ValueError`
3. `unit` debe ser `"metric"` o `"imperial"` — si no, lanza `ValueError`

### Salida esperada

```python
calculate_bmi(70, 1.75)
# {"bmi": 22.86, "category": "Normal weight", "unit": "metric"}

calculate_bmi(154, 69, unit="imperial")
# {"bmi": 22.74, "category": "Normal weight", "unit": "imperial"}

calculate_bmi(-70, 1.75)
# ValueError: weight must be greater than 0

calculate_bmi(70, 1.75, unit="random")
# ValueError: unit must be metric or imperial
```

### Requisitos

- Usa type hints con parámetro opcional
- Lanza `ValueError` con mensajes descriptivos en inglés
- Usa un dispatch table para los sistemas de unidades
- Usa una lista de tuplas para los rangos de categorías — sin cadenas de `if/elif` para las categorías

---

## Submit your solution

Place your file at:

```
solutions/python/your_github_username.py
```

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full instructions.
