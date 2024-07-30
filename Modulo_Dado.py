# Módulo_dados.py

import random

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
