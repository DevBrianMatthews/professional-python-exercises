# E08 — Slug Generator

**Difficulty:** Easy  
**Topics:** `re.sub()`, `str.maketrans()`, `str.translate()`, string manipulation, type hints

---

## 🇬🇧 English

### Context

Slugs are clean URLs generated from text — used in blogs, e-commerce platforms, CMSs, and any system that builds URLs from titles or names. It's a text transformation that appears in almost every web backend.

### Task

Write a function `generate_slug(text: str, max_length: int = 60) -> str` that receives a text string and returns its slug version.

### Transformation rules

1. Convert to lowercase
2. Replace accented characters with their unaccented equivalent (`á→a`, `é→e`, `í→i`, `ó→o`, `ú→u`, `ñ→n`, `ü→u`)
3. Replace any character that is not a letter or number with a hyphen `-`
4. Collapse consecutive duplicate hyphens into one
5. Remove hyphens at the start and end
6. If the result exceeds `max_length`, cut at that limit without leaving a trailing hyphen

### Validation rules

1. If `text` is empty or contains only spaces, raise `ValueError`
2. `max_length` must be greater than `0` — otherwise raise `ValueError`

### Expected output

```python
generate_slug("Hello World!")
# "hello-world"

generate_slug("¿Cómo estás, Alejandra?")
# "como-estas-alejandra"

generate_slug("  --  espacios  --  ")
# "espacios"

generate_slug("Este es un título muy largo que supera el límite", max_length=20)
# "este-es-un-titulo-mu"

generate_slug("")
# ValueError: text cannot be empty
```

### Requirements

- Use type hints with an optional parameter
- Raise `ValueError` with descriptive messages in English
- Use `re.sub()` for character replacement
- Use `str.maketrans()` and `str.translate()` for accent removal
- Apply transformations in the correct order — order matters here

---

## 🇪🇸 Español

### Contexto

Los slugs son URLs limpias generadas a partir de texto — se usan en blogs, e-commerce, CMSs y cualquier sistema que construya URLs a partir de títulos o nombres. Es una transformación de texto que aparece en casi cualquier backend web.

### Tarea

Escribe una función `generate_slug(text: str, max_length: int = 60) -> str` que reciba un texto y retorne su versión slug.

### Reglas de transformación

1. Convertir a minúsculas
2. Reemplazar caracteres acentuados por su equivalente sin acento (`á→a`, `é→e`, `í→i`, `ó→o`, `ú→u`, `ñ→n`, `ü→u`)
3. Reemplazar cualquier carácter que no sea letra o número por un guión `-`
4. Eliminar guiones duplicados consecutivos
5. Eliminar guiones al inicio y al final
6. Si el resultado supera `max_length`, cortar en ese límite sin dejar un guión al final

### Reglas de validación

1. Si `text` está vacío o es solo espacios, lanza `ValueError`
2. `max_length` debe ser mayor a `0` — si no, lanza `ValueError`

### Salida esperada

```python
generate_slug("Hello World!")
# "hello-world"

generate_slug("¿Cómo estás, Alejandra?")
# "como-estas-alejandra"

generate_slug("  --  espacios  --  ")
# "espacios"

generate_slug("Este es un título muy largo que supera el límite", max_length=20)
# "este-es-un-titulo-mu"

generate_slug("")
# ValueError: text cannot be empty
```

### Requisitos

- Usa type hints con parámetro opcional
- Lanza `ValueError` con mensajes descriptivos en inglés
- Usa `re.sub()` para el reemplazo de caracteres
- Usa `str.maketrans()` y `str.translate()` para eliminar acentos
- Aplica las transformaciones en el orden correcto — el orden importa aquí

---

## Submit your solution

Place your file at:

```
solutions/python/your_github_username.py
```

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full instructions.
