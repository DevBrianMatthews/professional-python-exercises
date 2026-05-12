# E05 — Text Analyzer

**Difficulty:** Easy  
**Topics:** `string`, `str.translate()`, `str.maketrans()`, `dict`, `max()`, `split()`, type hints

---

## 🇬🇧 English

### Context

Extracting metrics from text is a frequent task in professional development — processing logs, analyzing user-generated content, building reporting tools, or working with documents. This challenge reinforces string manipulation and dictionary-based counting patterns.

### Task

Write a function `analyze_text(text: str) -> dict` that receives a string and returns a dictionary with the following metrics:

- `word_count` — total number of words
- `char_count` — total number of characters, not counting spaces or punctuation
- `sentence_count` — number of sentences (ending in `.`, `!`, `?` or `,`)
- `most_common_word` — the most repeated word (lowercase, ignoring punctuation)
- `average_word_length` — average word length, rounded to 2 decimal places

### Rules

1. If `text` is empty or contains only spaces, raise `ValueError`
2. For `most_common_word`, ignore punctuation attached to words (`"hello,"` counts as `"hello"`)
3. In case of a tie in `most_common_word`, return the one that appears first in the text

### Expected output

```python
analyze_text("Hello world. Hello Python!")
# {
#     "word_count": 4,
#     "char_count": 22,
#     "sentence_count": 2,
#     "most_common_word": "hello",
#     "average_word_length": 5.5
# }

analyze_text("   ")
# ValueError: text cannot be empty
```

### Requirements

- Use type hints
- Raise `ValueError` with a descriptive message in English
- Use `str.maketrans()` and `str.translate()` to strip punctuation
- No external libraries except `string`

---

## 🇪🇸 Español

### Contexto

Extraer métricas de texto es una tarea frecuente en el desarrollo profesional — procesar logs, analizar contenido generado por usuarios, construir herramientas de reporte o trabajar con documentos. Este reto refuerza la manipulación de strings y los patrones de conteo con diccionarios.

### Tarea

Escribe una función `analyze_text(text: str) -> dict` que reciba un string y retorne un diccionario con las siguientes métricas:

- `word_count` — número total de palabras
- `char_count` — número total de caracteres sin contar espacios ni puntuación
- `sentence_count` — número de oraciones (terminan en `.`, `!`, `?` o `,`)
- `most_common_word` — la palabra más repetida (en minúsculas, ignorando puntuación)
- `average_word_length` — promedio de longitud de palabras, redondeado a 2 decimales

### Reglas

1. Si `text` está vacío o es solo espacios, lanza `ValueError`
2. Para `most_common_word`, ignora puntuación pegada a las palabras (`"hola,"` cuenta como `"hola"`)
3. En caso de empate en `most_common_word`, retorna la que aparece primero en el texto

### Salida esperada

```python
analyze_text("Hola mundo. Hola Python!")
# {
#     "word_count": 4,
#     "char_count": 18,
#     "sentence_count": 2,
#     "most_common_word": "hola",
#     "average_word_length": 4.5
# }

analyze_text("   ")
# ValueError: text cannot be empty
```

### Requisitos

- Usa type hints
- Lanza `ValueError` con mensaje descriptivo en inglés
- Usa `str.maketrans()` y `str.translate()` para eliminar puntuación
- Sin librerías externas excepto `string`

---

## Submit your solution

Place your file at:

```
solutions/python/your_github_username.py
```

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full instructions.
