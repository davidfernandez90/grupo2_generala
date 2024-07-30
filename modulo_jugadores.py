# Funciones del módulo jugadores.py
def crear_jugadores(num_jugadores):
    jugadores = []
    for i in range(num_jugadores):
        nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
        jugadores.append(nombre)
    return jugadores