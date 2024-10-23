""" Dado  el  siguiente  diccionario,  cuyos  elementos  asocian  a  cada  goleador  del  mundial  la
respectiva cantidad de goles convertidos:
goleadores = { "Rodríguez" : 6, "Messi" : 4, "Neymar" : 4, "Müller": 4,  ... }
a. Dada la variable gol = "Higuaín", incrementar en uno la cantidad de goles
correspondientes al jugador representado en gol, verificando si ya existe en el diccionario.
b. Dada la variable cambio = ("Roben", "Robben"), eliminar del diccionario, si existe, los datos correspondientes a la primera componente de la tupla y asociarlos, en el diccionario, a la segunda componente de la tupla.
c. Explique cómo determinaría cuál es el/los máximo/s goleador/es del mundial. """

def incrementarGol(goleadores, gol):
    if (gol in goleadores):
        goleadores[gol] += 1

def cambiarJugador(goleadores, cambio):
    jugador_actual = cambio[0]
    jugador_cambio = cambio[1]
    if (jugador_actual in goleadores):
        goleadores[jugador_cambio] = goleadores[jugador_actual]
        goleadores.pop(jugador_actual)

def mostrar_goleadores():
    goleadores = { "Rodríguez" : 6, "Messi" : 4, "Neymar" : 4, "Müller": 4, "Higuaín": 306, "Roben": 209 }
    gol = "Higuaín"
    incrementarGol(goleadores, gol)
    cambio = ("Roben", "Robben")
    cambiarJugador(goleadores, cambio)
    print(goleadores)

mostrar_goleadores()