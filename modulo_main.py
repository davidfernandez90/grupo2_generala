import random
import time
import os
import pickle
from módulo_puntajes import verificar_combinaciones
from modulo_turnos import jugar_turno
from modulo_juegos import mostrar_puntajes , jugar_generala
from Módulo_utilidades import validar_numero
from Modulo_Dado import lanzar_dados , mostrar_dados , obtener_frecuencias
from modulo_jugadores import crear_jugadores

# Archivo principal
def guardar_estado(filename, estado):
    with open(filename, 'wb') as file:
        pickle.dump(estado, file)

def cargar_estado(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
    
def main():
    os.system('cls')
    print("                         Bienvenidos a la generala")    
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
