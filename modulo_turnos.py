# Funciones del módulo turnos.py
def jugar_turno(jugador, usadas):
    dados = lanzar_dados()
    mostrar_dados(dados)
    for _ in range(2):
        while True:
            reroll = input("¿Quieres volver a lanzar algunos dados? (si/no): ").strip().lower()
            if reroll in ('si', 'no'):
                break
            print("Respuesta no válida. Por favor, ingresa 'si' o 'no'.")

        if reroll == 'no':
            os.system('cls')
            break
        while True:
            indices = input("Ingresa los índices de los dados a relanzar (0-4) separados por comas: ")
            try:
                indices = list(map(int, indices.split(',')))
                if any(i < 0 or i > 4 for i in indices):
                    raise ValueError
                os.system('cls')
                break
            except ValueError:
                print("Entrada incorrecta. Por favor, ingrese índices válidos (0-4) separados por comas.")
        for i in indices:
            dados[i] = random.randint(1, 6)
        mostrar_dados(dados)
    combinacion, puntaje = verificar_combinaciones(dados, usadas)
    if combinacion != "Nada":
        usadas.add(combinacion)
    print(f"{jugador} obtiene {combinacion} con un puntaje de {puntaje}")
    time.sleep(1)
    os.system('cls')
    return puntaje