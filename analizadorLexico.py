import re

def tokenize(input_str):
    # Lista de patrones para reconocer tokens
    token_patterns = [
        (r'struct\?', 'STRUCT'),                 # Palabra clave struct
        (r'int\+|string\+', 'VAR_TYPE'),             # Palabras clave
        (r'[a-zA-Z_][a-zA-Z0-9_]*', 'VAR_IDENTIFIER'),  # Identificadores (nombres de variables)
        (r'\d+', 'NUMBER'),                  # Números enteros
        (r'".*?"', 'STRING'),                # Cadenas entre comillas dobles
        (r'[\(]', 'PAREN_OPEN'),         # (
        (r'[\)]', 'PAREN_CLOSE'),         # )
        (r'[\{]', 'CBRACES_OPEN') ,        # {
        (r'[\}]', 'CBRACES_CLOSE')  ,       # }
        (r'[\=]', 'EQUALS')     ,    # =
        (r'[\,]', 'COMMA')    ,     # ,
        (r'[\+]', 'PLUS')      ,   # +
    ]

    tokens = []
    current_position = 0

    while current_position < len(input_str):
        match = None

        # Ignorar espacios en blanco y otros caracteres no deseados
        if input_str[current_position].isspace():
            current_position += 1
            continue

        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(input_str, current_position)
            if match:
                value = match.group(0)
                tokens.append((value, token_type))
                current_position = match.end()
                break
        
        if not match:
            raise Exception('Carácter no válido: ' + input_str[current_position])
    
    return tokens
