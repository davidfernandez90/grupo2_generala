import random
import time
import os
import pickle


# Funciones del módulo dados.py
def lanzar_dados(num_dados=5):
    return [random.randint(1, 6) for _ in range(num_dados)]

def mostrar_dados(dados):
    print("Resultados del lanzamiento: ", dados)

def obtener_frecuencias(dados):
    frecuencias = {}
    for dado in dados:
        if dado in frecuencias:
            frecuencias[dado] += 1
        else:
            frecuencias[dado] = 1
    return frecuencias

# Funciones del módulo puntajes.py
def verificar_combinaciones(dados, usadas):
    frecuencias = obtener_frecuencias(dados)
    valores = list(frecuencias.values())

    if 5 in valores and "Generala" not in usadas:
        return ("Generala", 50)
    elif 4 in valores and "Poker" not in usadas:
        return ("Poker", 40)
    elif 3 in valores and 2 in valores and "Full" not in usadas:
        return ("Full", 30)
    elif sorted(dados) in [list(range(1, 6)), list(range(2, 7))] and "Escalera" not in usadas:
        return ("Escalera", 20)
    elif 3 in valores and "Trío" not in usadas:
        return ("Trío", 10)
    elif valores.count(2) == 2 and "Doble Pareja" not in usadas:
        return ("Doble Pareja", 5)
    elif 2 in valores and "Par" not in usadas:
        return ("Par", 2)
    else:
        return ("Nada", 0)

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
                return

# Funciones del módulo jugadores.py
def crear_jugadores(num_jugadores):
    jugadores = []
    for i in range(num_jugadores):
        nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
        jugadores.append(nombre)
    return jugadores

# Funciones del módulo utilidades.py
def validar_numero(prompt, min_val=None, max_val=None):
    while True:
        try:
            valor = int(input(prompt))
            if (min_val is not None and valor < min_val) or (max_val is not None and valor > max_val):
                print(f"Por favor, ingrese un número entre {min_val} y {max_val}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")



# Archivo principal main.py
def guardar_estado(filename, estado):
    with open(filename, 'wb') as file:
        pickle.dump(estado, file)

def cargar_estado(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
    
def main():
    os.system('cls')
    texto= '                         Bienvenidos a la generala'
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.1)
    time.sleep(1)
    os.system('cls')

    while True:
        print("Elige una opcion de 1 al 3 para continuar.")
        time.sleep(1)
       
        
        time.sleep(1) 
        print("Juego Nuevo ->1\n")
        time.sleep(1)        
        print("Continuar Juego ->2\n")
        time.sleep(1)
        print("Salir->3\n")
        time.sleep(1)
        
        
        opcion=input("Ingrese su opcion: ")
       
        os.system('cls')
        if opcion == '1':
            num_jugadores = validar_numero("Ingrese el número de jugadores: ", min_val=1)
            jugadores = crear_jugadores(num_jugadores)
            puntaje_maximo = validar_numero("Ingrese el puntaje máximo para ganar: ", min_val=1)
            jugar_generala(jugadores, puntaje_maximo)
        elif opcion == '2':
            try:
                estado = cargar_estado('estado_juego.pkl')
                jugar_generala(
                    estado['jugadores'],
                    estado['puntaje_maximo'],
                    estado['puntajes'],
                    estado['combinaciones_usadas'],
                    estado['turnos']
                )
            except FileNotFoundError:
                print("No hay ningún juego guardado.")
        
        elif opcion == '3':
            break
        else:
            print("El número ingresado no corresponde a una opción del menú. Ingrese nuevamente.")

if __name__ == "__main__":
    main()