titles = [
    "Speedrun de Super Mario en tiempo récord",
    "Charla sobre desarrollo de videojuegos",
    "Jugando al nuevo FPS del momento con amigos",
    "Música en vivo: improvisaciones al piano",
]

# Busco el titulo con mas palabras
line_max = max(titles, key = lambda title: len(title.split()))

print(f"El título más largo es: \"{line_max}\"")
