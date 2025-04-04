import random
import string

def generate_date(name,date):
    """
    Genera un codigo de descuento aleatorio de 30 caracteres en base
    al nombre de usuario y la fecha ingresados.

    por ejemplo:

    name = python

    date = 20-03-2025

    resultado = PYTHON-20032025-XXXXXXXXXXXXXX

    Siendo "X" una letra mayuscula o número aleatorio.
    """
    if(len(name) <= 15):
        code =  name.upper()+"-"+date.replace("-","")
        if(len(code) < 30):
            possible_characters = string.ascii_uppercase + string.digits
            code += "-"+"".join(random.sample(possible_characters,30 - len(code)))
        return code
    else:
       print("El nombre de usuario debe tener menos de 15 caracteres") 


name = input("Ingrese el nombre de usuario: ")
date = input("Ingrese la fecha: ")
print(f"Código de descuento: {generate_date(name,date)}")