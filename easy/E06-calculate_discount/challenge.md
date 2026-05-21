# E06 — Discount Calculator

**Difficulty:** Easy  
**Topics:** arithmetic, `round()`, `ValueError`, default parameters, type hints

---

## 🇬🇧 English

### Context

Any e-commerce or point-of-sale system handles discounts, taxes, and final prices. Getting the order of operations wrong — applying tax before discount, or mixing up percentages with fixed values — causes real billing bugs in production.

### Task

Write a function `calculate_discount(price: float, discount: float, tax: float = 0.0) -> dict` that receives the original price, a discount percentage, and an optional tax percentage, and returns:

- `original_price` — the original price
- `discount_amount` — the monetary value of the discount applied
- `tax_amount` — the monetary value of the tax applied on the discounted price
- `final_price` — the final price after discount and tax

### Rules

1. `price` must be greater than `0` — otherwise raise `ValueError`
2. `discount` must be between `0` and `100` — otherwise raise `ValueError`
3. `tax` must be between `0` and `100` — otherwise raise `ValueError`
4. Tax is applied **after** the discount, not on the original price
5. All values in the result must be rounded to 2 decimal places

### Expected output

```python
calculate_discount(100.0, 20.0)
# {
#     "original_price": 100.0,
#     "discount_amount": 20.0,
#     "tax_amount": 0.0,
#     "final_price": 80.0
# }

calculate_discount(100.0, 20.0, 19.0)
# {
#     "original_price": 100.0,
#     "discount_amount": 20.0,
#     "tax_amount": 15.2,
#     "final_price": 95.2
# }

calculate_discount(-50.0, 20.0)
# ValueError: price must be greater than 0

calculate_discount(100.0, 110.0)
# ValueError: discount must be between 0 and 100
```

### Requirements

- Use type hints with an optional parameter
- Raise `ValueError` with descriptive messages in English
- Apply operations in the correct order — discount first, tax after

---

## 🇪🇸 Español

### Contexto

Cualquier sistema de e-commerce o punto de venta maneja descuentos, impuestos y precios finales. Aplicar el impuesto antes del descuento, o confundir porcentajes con valores fijos, genera bugs reales de facturación en producción.

### Tarea

Escribe una función `calculate_discount(price: float, discount: float, tax: float = 0.0) -> dict` que reciba el precio original, el porcentaje de descuento y un porcentaje de impuesto opcional, y retorne:

- `original_price` — precio original
- `discount_amount` — valor monetario del descuento aplicado
- `tax_amount` — valor monetario del impuesto aplicado sobre el precio con descuento
- `final_price` — precio final después de descuento e impuesto

### Reglas

1. `price` debe ser mayor a `0` — si no, lanza `ValueError`
2. `discount` debe estar entre `0` y `100` — si no, lanza `ValueError`
3. `tax` debe estar entre `0` y `100` — si no, lanza `ValueError`
4. El impuesto se aplica **después** del descuento, no sobre el precio original
5. Todos los valores del resultado se redondean a 2 decimales

### Salida esperada

```python
calculate_discount(100.0, 20.0)
# {
#     "original_price": 100.0,
#     "discount_amount": 20.0,
#     "tax_amount": 0.0,
#     "final_price": 80.0
# }

calculate_discount(100.0, 20.0, 19.0)
# {
#     "original_price": 100.0,
#     "discount_amount": 20.0,
#     "tax_amount": 15.2,
#     "final_price": 95.2
# }

calculate_discount(-50.0, 20.0)
# ValueError: price must be greater than 0

calculate_discount(100.0, 110.0)
# ValueError: discount must be between 0 and 100
```

### Requisitos

- Usa type hints con parámetro opcional
- Lanza `ValueError` con mensajes descriptivos en inglés
- Aplica las operaciones en el orden correcto — descuento primero, impuesto después

---

## Submit your solution

Place your file at:

```
solutions/python/your_github_username.py
```

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full instructions.
