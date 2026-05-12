import string
def analyze_text(text: str) -> dict:

    if not text.strip():
        raise ValueError('text cannot be empty.')

    text_lower = text.lower() # Convertir en minusculas
    text_list  = text_lower.split(' ') # Convertir texto en lista

    # Eliminar simbolos
    clear       = str.maketrans('', '', string.punctuation)
    clean_text  = text_lower.translate(clear) # Texto limpio sin simbolos

    black_list  = clean_text.split(' ') # Lista con elementos vacios
    clean_list  = [x for x in black_list if x != ''] # Eliina elementos vacios de la lista

    word_dict   = {}

    # Cantidad de letras
    plain_text = "".join(clean_list) # Crea un nuevo texto eliminando los espacios
    flag_char = len(plain_text)

    # Cantidad de palabras
    word_count = len(clean_list)

    # Cantidad de oraciones
    sentences = sum(x in ',.!?' for x in plain_text)

    # Contar palabras repetidas
    for word in clean_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    repeated = max(word_dict, key=word_dict.get)

    # → Saber la longitud promedio
    flag_count = 0
    for i in clean_list:
        flag_count += len(i)

    long = round(flag_count / len(clean_list), 2)

    result_dict = {
        'word_count':          word_count,
        'char_count':          flag_char,
        'sentence_count':      sentences,
        'most_common_word':    repeated,
        'average_word_length': long
        }

    return result_dict