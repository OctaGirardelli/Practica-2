rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""

key_word = input("Ingrese una palabra clave: ").lower()

rules = [rule for rule in rules.split("\n") if key_word in rule.lower()]

for rule in rules:
    print(rule)

