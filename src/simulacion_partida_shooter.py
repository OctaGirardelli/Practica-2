def update_ranking(ranking,round):
    """
    Actualiza el ranking recibido como parametro en base a una ronda recibida como parametro.

    Para cada jugador, suma las kills, asistencias y muertes de la ronda. Tambien determina el MVP de la ronda, suma
    1 a su contador de MVPs y lo retorna.

    Parameters:
        ranking(dict): El ranking total de jugadores.
        round(dict): La ronda actual.
    Returns:
        str: Nombre del jugador MVP.
    """
    KILL_POINTS = 3
    max_score = -1
    mvp = ''
    for key,value in round.items():
        # Actualiza kills, asistencias, muertes
        ranking[key]['kills'] += value['kills']
        ranking[key]['assists'] += value['assists']
        ranking[key]['deaths'] += 1 if value['deaths'] else 0
        
        # Calcula y actualiza puntaje
        score = (value['kills'] * KILL_POINTS) + value['assists'] - (1 if value['deaths'] else 0)
        ranking[key]['points'] += score

        # Determina el MVP de la ronda
        if score > max_score:
            max_score = score
            mvp = key
    ranking[mvp]['MVPs'] += 1
    return mvp


def print_ranking(ranking,number):
    """
    Imprime el ranking de jugadores en forma de tabla.

    La tabla muestra para cada jugador: kills, asistencias, muertes, cantidad
    de MVPs y puntos totales, ordenados en forma decreciente por puntos.

    Parameters:
        ranking(dict): El ranking total de jugadores.
        number(str): El numero actual de ronda(por ejemplo 'ronda 3' o 'final').
    """
    # Encabezado de la tabla
    print(f'Ranking {number}: \nJugador Kills Asistencias Muertes MVPs Puntos\n','-' * 60)

    # Nombre y valores de cada jugador alineados en las columnas
    for key in sorted(ranking,key=lambda c: ranking[c]['points'],reverse=True):
        print(f'{key}{' '*(10-len(key))}{ranking[key]['kills']}{ranking[key]['assists']:>9}{ranking[key]['deaths']:>10}{ranking[key]['MVPs']:>6}{ranking[key]['points']:>7}')
    
    print('-' * 60)
    

if __name__ == "__main__":
    # Conjunto de rondas
    rounds = [
        {
            'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
            'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
            'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
            'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
            'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
        },
        {
            'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
            'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
            'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
            'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
            'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
        },
        {
            'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
            'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
            'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
            'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
            'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
        },
        {
            'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
            'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
            'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
            'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
            'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
        },
        {
            'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
            'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
            'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
            'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
            'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
        }
    ]

    #Si no hay rondas, no se hace nada
    if len(rounds) != 0:
        # El ranking comienza como un diccionario que tiene nombre : diccionario de valores(0 todos por defecto)
        ranking = dict((character,{'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs': 0, 'points': 0}) for character in rounds[0].keys())

        # Simula cada ronda y muestra el ranking
        for i in range(len(rounds)-1):
            mvp = update_ranking(ranking,rounds[i])
            print_ranking(ranking,f"ronda {i+1}")
            print(f"El MVP de la ronda {i+1} fue {mvp}")
        # Ronda final
        mvp = update_ranking(ranking,rounds[-1])
        print_ranking(ranking,"final")
        print(f"El MVP de la ronda final fue {mvp}")
