""" Definir una función, denominada "diferencia_conj", que dadas como parámetros dos listas,
devuelva como resultado una nueva lista, constituida por los valores que están en la primera
lista y no están en la segunda, evitando las repeticiones. [No es necesario validar los datos]
Ejemplo:   Dadas  las  listas   [ "alfa", "beta", 1, "alfa", 3 ]   y   [ 1, "beta", "omega", 9 ]
la función debería devolver      [ "alfa", 3 ] """

def diferencia_conj(lista1, lista2):
    lista3 = []
    for i in lista1:
        if (i not in lista2 and i not in lista3):
            lista3.append(i)
    return lista3

lista1 = [ "alfa", "beta", 1, "alfa", 3 ]
lista2 = [ 1, "beta", "omega", 9 ]
print(diferencia_conj(lista1, lista2))