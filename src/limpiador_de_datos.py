clients = [
    " Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
    " Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
    "luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
    " ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA RAMOS",
    "carlos mendes", "RICARDO FERNÁNDEZ ", " Laura ramos", "CARLOS MENDES",
    "alejandro gonzález", " ALEJANDRO GONZÁLEZ ", "Patricia Vega",
    "patricia VEGA", "Andrés Ocampo", " andrés ocampo", "Monica Herrera",
    "MONICA HERRERA ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
    "SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
    "Damián Castillo ", None, "", " "
]

def remove_null_or_empty(clients):
    """
    Devuelve una copia de la lista de clientes recibida como parametro sin
    los elementos nulos, vacios o que solo contengan espacios.

    Por ejemplo:

    clients = ["Maria Morales","",None," ","  "]

    salida: ["Maria Morales"]
    """
    return [c for c in clients if c and c.strip()]

def remove_spaces(clients):
    return [c.strip() for c in clients]

def convert_to_title(clients):
    """
    Devuelve una copia de la lista de clientes recibida como parametro con
    el formato de titulo(Primer letra de cada nombre o apellido en mayúscula).

    Por ejemplo:

    clients = ["MARIA MORALES","juan perez"]

    salida: ["Maria Morales","Juan Perez"]
    """
    return [c.title() for c in clients]

def normalize_name(name):
    """
    Devuelve una copia del nombre recibido como parámetro sin tildes.
    Por ejemplo:

    name = "María Gonzáles"

    salida: "Maria Gonzales"
    """
    return name.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")

def remove_repeated(clients):
    """
    Devuelve una copia de la lista de clientes recibida como parametro sin
    los elementos repetidos, sin diferenciar por tildes. En caso de haber elementos
    repetidos solo se almacena el primero encontrado.

    Por ejemplo:

    clients = ["María Gonzáles","Juan Perez","Maria Gonzáles","Juan Pérez"]

    salida: ["María Gonzáles","Juan Perez"]
    """
    names_set = set()
    non_repeated = []
    for c in clients:
        if not (normalize_name(c) in names_set):
            names_set.add(normalize_name(c))
            non_repeated.append(c)
    return non_repeated




# En el enunciado no pedía que se ordenara la lista de nombres, pero la ordeno porque asi se ve en el ejemplo
clients = sorted(remove_repeated(convert_to_title(remove_spaces(remove_null_or_empty(clients)))))


print("Lista limpia de clientes al realizar todas las operaciones: ")
print()
print(clients)
