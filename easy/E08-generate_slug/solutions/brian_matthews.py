import re

def generate_slug(text: str, max_length: int = 60) -> str:
    if not text.strip():
        raise ValueError('text cannot be empty.')

    if max_length <= 0:
        raise ValueError('The length must be greater than zero.')

    lower_text = text.lower()
    clear      = str.maketrans('áéíóúñü', 'aeiounu')
    clear_text = lower_text.translate(clear)
    clean_text = re.sub(r'[^a-z0-9]+', '-', clear_text)

    if len(clean_text) > max_length:
        clean_text = clean_text[:max_length]
        clean_text = clean_text.strip('-')

    return clean_text

print(generate_slug('Esté es un títúlo muy lar$$go que supera el límite', 20))