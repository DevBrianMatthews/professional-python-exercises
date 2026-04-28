# E02 — Tip Calculator

**Difficulty:** Easy  
**Topics:** arithmetic, `round()`, `ValueError`, type hints, input validation

---

## 🇬🇧 English

### Context

Any system that handles money needs to validate numeric inputs and return clean, formatted results. This pattern appears constantly in e-commerce, fintech, and restaurant apps. Getting the rounding wrong or skipping validation causes real bugs in production.

### Task

Write a function `calculate_tip(bill: float, tip_percent: float, people: int) -> dict` that receives the bill amount, tip percentage, and number of people, and returns a dictionary with:

- `tip_total` — total tip amount
- `tip_per_person` — tip per person
- `bill_per_person` — total each person pays (bill + tip)
- `total` — full total (bill + tip)

### Validation rules

1. `bill` must be greater than `0`
2. `tip_percent` must be between `0` and `100`
3. `people` must be an integer greater than `0`
4. If any value is invalid, raise a `ValueError` with a descriptive message in English
5. All values in the result must be rounded to 2 decimal places

### Expected output

```python
calculate_tip(100.0, 15.0, 4)
# {
#     "tip_total": 15.0,
#     "tip_per_person": 3.75,
#     "bill_per_person": 28.75,
#     "total": 115.0
# }

calculate_tip(-50.0, 15.0, 4)
# ValueError: "bill must be greater than 0"

calculate_tip(100.0, 15.0, 0)
# ValueError: "people must be greater than 0"
```

### Requirements

- Use type hints
- Raise `ValueError` with descriptive messages for each invalid case
- No external libraries

---

## 🇪🇸 Español

### Contexto

Cualquier sistema que maneje dinero necesita validar inputs numéricos y retornar resultados limpios y formateados. Este patrón aparece constantemente en e-commerce, fintech y apps de restaurantes. Redondear mal u omitir validaciones genera bugs reales en producción.

### Tarea

Escribe una función `calculate_tip(bill: float, tip_percent: float, people: int) -> dict` que reciba el valor de una cuenta, el porcentaje de propina y el número de personas, y retorne un diccionario con:

- `tip_total` — valor total de la propina
- `tip_per_person` — propina por persona
- `bill_per_person` — total a pagar por persona (cuenta + propina)
- `total` — total general (cuenta + propina)

### Reglas de validación

1. `bill` debe ser mayor a `0`
2. `tip_percent` debe estar entre `0` y `100`
3. `people` debe ser un entero mayor a `0`
4. Si algún valor es inválido, lanza un `ValueError` con un mensaje descriptivo en inglés
5. Los valores del resultado se redondean a 2 decimales

### Salida esperada

```python
calculate_tip(100.0, 15.0, 4)
# {
#     "tip_total": 15.0,
#     "tip_per_person": 3.75,
#     "bill_per_person": 28.75,
#     "total": 115.0
# }

calculate_tip(-50.0, 15.0, 4)
# ValueError: "bill must be greater than 0"

calculate_tip(100.0, 15.0, 0)
# ValueError: "people must be greater than 0"
```

### Requisitos

- Usa type hints
- Lanza `ValueError` con mensajes descriptivos para cada caso inválido
- Sin librerías externas

---

## Submit your solution

Place your file at:
```
solutions/python/your_github_username.py
```

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full instructions.
