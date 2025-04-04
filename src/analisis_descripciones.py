descriptions = [
    "Streaming de música en vivo con covers y composiciones",
    "Charla interactiva con la audiencia sobre series y películas",
    "Jugamos a juegos retro y charlamos sobre su historia",
    "Exploramos la mejor música de los 80s y 90s",
    "Programa de entretenimiento con noticias y curiosidades del mundo gamer",
    "Sesión de charla con invitados especiales del mundo del streaming",
    "Música en directo con improvisaciones y peticiones del chat",
    "Un espacio para charlar relajada sobre tecnología y cultura digital",
    "Exploramos el impacto de la música en los videojuegos clásicos"
]


def count_mentions(words):
    """
    Cuenta las menciones de cada palabra en las descripciones de streams.

    Recorre la lista global 'descriptions' (se espera que exista) y cuenta
    cuántas veces aparece cada palabra.
    
    Devuelve el conteo como un diccionario en el formato
    'palabra : cantidad de veces encontrada'.

    """
    amounts = dict((word,0) for word in words)
    for description in descriptions:
        description = description.lower().split()
        for word in words:
            if(word in description):
                amounts[word] += 1
    return amounts


amounts = count_mentions(("entretenimiento","música","charla"))

for key,value in amounts.items():
    print(f"Menciones de '{key}': {value}")