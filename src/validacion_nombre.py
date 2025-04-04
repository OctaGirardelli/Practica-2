def is_valid_name(name):
    """
    Verifica si un nombre de usuario es válido.

    Un nombre de usuario se considera válido si:
        - Tiene al menos 5 caracteres.
        - Contiene solo caracteres alfanumericos.
        - Incluye al menos una letra mayuscula.
        - Incluye al menos un numero.
    """
    has_digit=False
    has_upper=False

    if len(name) >= 5 and name.isalnum():
        for c in name:
            has_upper = has_upper or c.isupper()
            has_digit = has_digit or c.isdigit()
        return has_digit and has_upper
    return False

name = input("Ingrese el nombre de usuario: ")

print("El nombre de usuario es válido." if is_valid_name(name) else "El nombre de usuario no cumple con los requisitos.")

