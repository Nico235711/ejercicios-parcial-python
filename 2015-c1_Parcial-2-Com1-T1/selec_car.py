""" Definir una función, denominada "selec_car", que reciba como parámetros una cadena de
caracteres y una tupla de números enteros, que representan posiciones, y devuelva como
resultado una cadena, compuesta por los caracteres de la cadena parámetro ubicados en
las posiciones indicadas por la tupla. [No es necesario validar los datos.]
Ejemplo:   Dadas  la  cadena = "a seleccionar esto"  y   la tupla = (2, 3, 4, 5, 6, -2, -1)
la función debería devolver   'selecto' """

def selec_car(cadena, tupla):
    cadena_nueva = ""
    for i in tupla:
        cadena_nueva += cadena[i]
    return cadena_nueva

cadena = "a seleccionar esto"
tupla = (2, 3, 4, 5, 6, -2, -1)
print(selec_car(cadena, tupla))