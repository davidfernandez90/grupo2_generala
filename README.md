# grupo2_generala
Desarrollo del juego de La Generala modularizado en Python.
# Generala

## Descripción del Proyecto

Generala es un juego de dados clásico que se juega con cinco dados. El objetivo es obtener ciertas combinaciones de dados para obtener puntos. El juego permite a varios jugadores competir entre sí y el primer jugador en alcanzar un puntaje máximo determinado gana.

## Requisitos

- Python 3.x

## Instrucciones para Ejecutar el Programa

1. **Clona o descarga el repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   
2. Ejecuta el archivo principal:
python main.py

4. Sigue las instrucciones en pantalla para ingresar el número de jugadores, los nombres de los jugadores y el puntaje máximo para ganar.
   
## Estructura del Proyecto y los integrantes del equipo con sus funciones

El proyecto está organizado en los siguientes módulos:

dados.py:

Funciones para lanzar y mostrar los dados, así como para calcular la frecuencia de cada valor de dado.
Funciones:
lanzar_dados(num_dados=5): Lanza el número especificado de dados y devuelve una lista de resultados.
mostrar_dados(dados): Muestra los resultados de los dados.
obtener_frecuencias(dados): Calcula la frecuencia de cada valor en los dados.
Desarrollador: Maximiliano Mariani

puntajes.py:

Lógica para verificar combinaciones y asignar puntajes.
Funciones:
verificar_combinaciones(dados, usadas): Verifica las combinaciones posibles de dados y devuelve el tipo de combinación y su puntaje.
Desarrollador: Nahir Gonzalez

turnos.py:

Maneja el flujo de los turnos del juego, incluyendo el relanzamiento de dados.
Funciones:
jugar_turno(jugador, usadas): Controla un turno del jugador, permite el relanzamiento de dados y calcula el puntaje.
Desarrollador: David Fernandez

juego.py:

Controla el flujo principal del juego y el seguimiento de puntajes.
Funciones:
mostrar_puntajes(puntajes): Muestra los puntajes actuales de los jugadores.
jugar_generala(jugadores, puntaje_maximo): Coordina el juego, manejando turnos y actualizando puntajes.
Desarrollador: Alejandro Garnica

jugadores.py:

Permite crear y manejar la lista de jugadores.
Funciones:
crear_jugadores(num_jugadores): Crea una lista de jugadores a partir de la entrada del usuario.
Desarrollador: Rodrigo Echeverría

utilidades.py:

Proporciona funciones auxiliares, como la validación de entradas numéricas.
Funciones:
validar_numero(prompt, min_val=None, max_val=None): Valida la entrada numérica del usuario, asegurando que esté dentro del rango especificado.
Desarrollador: Matias Borgnia

main.py:

Archivo principal que inicia el juego y coordina los módulos.
Funciones:
main(): Inicia el juego, solicita información al usuario y llama a las funciones correspondientes para jugar.
Desarrollador: Marcelo Sobrero


