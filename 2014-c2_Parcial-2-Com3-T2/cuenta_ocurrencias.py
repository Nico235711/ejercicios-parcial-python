""" Definir  una  función,  denominada  "cuenta_ocurrencias",  que  dados  como  parámetros  una
cadena  de  caracteres  (que  representa  una  frase  integrada  por  letras  y  espacios)  y  una  tupla
compuesta  por  cadenas  de  caracteres  (que  representan  palabras),  devuelva  como  resultado
una lista de tuplas de dos componentes, constituidas con cada palabra y la respectiva cantidad
de  veces  que  esa  palabra  está  contenida  "exactamente"  como  subcadena  de  la  frase.  [No  es
necesario validar datos, ni considerar mayúsculas.]
Ejemplo:    Dados   cadena = "no se lamente la mente inteligente"
y    tuplita = ("ente", "ante", "mente", "gente")
la función debería devolver   [("ente", 3), ("ante", 0), ("mente", 2), ("gente", 1)] """

from cuantas_veces import cuantas_veces

def cuenta_ocurrencias(cadena, tuplaCadena):
    lista = []
    tupla = ()
    cantidad = 0
    for i in tuplaCadena:
        # print(i)
        cantidad = cuantas_veces(i, cadena)
        print(cantidad)

cadena = "no se lamente la mente inteligente"
tuplita = ("ente", "ante", "mente", "gente")
cuenta_ocurrencias(cadena, tuplita)