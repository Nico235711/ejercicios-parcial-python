""" Definir  una  función,  denominada  “disparo_naval”,  que  dados  como  parámetros  una  tupla
(compuesta por una letra y un número) que representa las coordenadas del disparo y una lista
que representa la ubicación de la flota (compuesta por listas de tuplas de dos elementos, que
representan  las  coordenadas  que  ocupa  cada  embarcación  militar),  devuelva  como  resultado
el valor 0 (cero) si el disparo va al agua, 1 (uno) si el disparo avería a una embarcación o 2
(dos)  si  el  disparo  hunde  una  embarcación.  Cuando  el  disparo  alcance  a  una  embarcación,
deberá  eliminar(3)  de  la  flota  (lista)  la  respectiva  tupla  de  coordenadas  [No  es  necesario
validar los datos.]
Ejemplos: Dada la flota = [ [ ("a",5), ("a",6), ("a",7) ], [ ("f",3) ], [ ("g",5), ("h",5) ] ]
Si   disparo = ("f", 3)    entonces   la función debería devolver:  2
Si   disparo = ("a", 7)    entonces   la función debería devolver:  1
Si   disparo = ("a", 8)    entonces   la función debería devolver:  0
Y sería el estado final de la flota = [ [ ("a",5), ("a",6) ], [ ], [ ("g",5), ("h",5) ] ] """

def disparo_naval(coordenada, flota):
    resultado_disparo = 0
    for embarcacion in flota:
        # cada embarcacion sera una lista
        if (coordenada in embarcacion):
            embarcacion.remove(coordenada)
            if (len(embarcacion) == 0):
                resultado_disparo = 2
            else:
                resultado_disparo = 1
    return resultado_disparo

flota = [ [ ("a",5), ("a",6), ("a",7) ], [ ("f",3) ], [ ("g",5), ("h",5) ] ]
disparo = ("f", 3)
print(f"1er. llamado: {disparo_naval(disparo, flota)}")

flota = [ [ ("a",5), ("a",6), ("a",7) ], [ ("f",3) ], [ ("g",5), ("h",5) ] ]
disparo = ("a", 7)
print(f"2do llamado: {disparo_naval(disparo, flota)}")

flota = [ [ ("a",5), ("a",6), ("a",7) ], [ ("f",3) ], [ ("g",5), ("h",5) ] ]
disparo = ("a", 8)
print(f"3er. llamado: {disparo_naval(disparo, flota)}")

