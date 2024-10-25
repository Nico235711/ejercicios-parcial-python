""" Definir una función “tabla_posic”, que reciba como parámetro un diccionario (la clave es la
selección y el valor es la cantidad de puntos) y una tupla compuesta por dos tuplas (de la
forma <selección, cantidad de goles>) representando el resultado del enfrentamiento, y
devuelva como resultado el diccionario actualizado con los nuevos puntajes de cada
selección (sumar al ganador 3 puntos, o 1 punto a cada uno en caso de empate). [No es
necesario validar los datos]
Ejemplo: Dados  la tupla   ( ( "Chile", 4 ) , ( "Panama", 2 ) )
y el diccionario   { "Argentina" : 9 , "Bolivia" : 0 , "Chile" : 3 , "Panama" : 3 }
    la función debería devolver (en cualquier orden):
{ "Argentina" : 9 , "Bolivia" : 0 , "Chile" : 6 , "Panama" : 3 }
"""

def sumarPuntos(diccionario, tupla):
    seleccion1 = tupla[0][0]
    seleccion2 = tupla[1][1]
    cantidad_goles_seleccion1 = tupla[0][1]
    cantidad_goles_seleccion2 = tupla[1][1]
    if (cantidad_goles_seleccion1 > cantidad_goles_seleccion2):
        diccionario[seleccion1] += 3
    elif (cantidad_goles_seleccion2 > cantidad_goles_seleccion1):
        diccionario[seleccion2] += 3
    else:
        diccionario[seleccion1] += 1
        diccionario[seleccion1] += 1
    return diccionario

def tabla_posic(diccionario, tupla):
    return sumarPuntos(diccionario, tupla)

tupla = ( ( "Chile", 4 ) , ( "Panama", 2 ) )
diccionario = { "Argentina" : 9 , "Bolivia" : 0 , "Chile" : 3 , "Panama" : 3 }
print(tabla_posic(diccionario, tupla))