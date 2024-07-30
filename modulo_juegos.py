# Funciones del módulo juego.py
def mostrar_puntajes(puntajes):
    print("Puntajes actuales:")
    for jugador, puntaje in puntajes.items():
        print(f"{jugador}: {puntaje} puntos")

def jugar_generala(jugadores, puntaje_maximo, puntajes=None, combinaciones_usadas=None, turnos=None):
    if puntajes is None:
        puntajes = {jugador: 0 for jugador in jugadores}
    if combinaciones_usadas is None:
        combinaciones_usadas = {jugador: set() for jugador in jugadores}
    if turnos is None:
        turnos = {jugador: 0 for jugador in jugadores}

    while True:
        for jugador in jugadores:
            os.system('cls')
            print(f"Turno de {jugador}:")
            if turnos[jugador] > 0:
                while True:
                    accion = input("¿Quieres (j)ugar tu turno, (v)er los puntajes o (g)uardar partida?: ")
                    if accion.lower() == 'v':
                        print("\n")
                        mostrar_puntajes(puntajes)
                    elif accion.lower() == 'j':
                        break
                    elif accion.lower() == 'g':
                        estado = {
                            'jugadores': jugadores,
                            'puntaje_maximo': puntaje_maximo,
                            'puntajes': puntajes,
                            'combinaciones_usadas': combinaciones_usadas,
                            'turnos': turnos
                        }
                        guardar_estado('estado_juego.pkl', estado)
                        print("Juego guardado.")
                        return
                    else:
                        print("Acción no válida. Por favor, elige (j)ugar, (v)er los puntajes o (g)uardar partida.")
            puntaje = jugar_turno(jugador, combinaciones_usadas[jugador])
            puntajes[jugador] += puntaje
            turnos[jugador] += 1
            if puntaje == 50 or puntajes[jugador] >= puntaje_maximo:
                print(f"¡{jugador} ha ganado el juego!")
                ganador = jugador
                return True #"devuelve"