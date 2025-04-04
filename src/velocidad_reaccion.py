reaction_time = input("Ingrese su tiempo de reacción en ms: ")

if(reaction_time.isdigit()):
    reaction_time = int(reaction_time)
    print("Categoria:",end = " ")
    print("Rápido" if reaction_time < 200 else "Lento" if reaction_time > 500 else "Normal")