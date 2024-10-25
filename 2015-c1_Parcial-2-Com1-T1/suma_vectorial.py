""" Definir una función, denominada “suma_vectorial”, que reciba como parámetros dos listas
de números enteros, ambas de igual longitud, y devuelva como resultado una lista
compuesta por las sumas de los elementos homólogos. [No es necesario validar los datos.]
Ejemplo:   Dadas  la lista = [ 1, 2, 9, 10, 3 ]  y   la lista = [ 2, 6, 3, 6, -2 ]
la función debería devolver  [ 3, 8, 12, 16, 1 ] """

def suma_vectorial(numeros1, numeros2):
    lista = []
    for i in range(len(numeros1)):
        lista.append(numeros1[i] + numeros2[i])
    return lista

lista1 = [ 1, 2, 9, 10, 3 ]
lista2 = [ 2, 6, 3, 6, -2 ]
print(suma_vectorial(lista1, lista2))