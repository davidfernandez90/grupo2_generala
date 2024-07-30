# Funciones del módulo puntajes
from Modulo_Dado import obtener_frecuencias

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
