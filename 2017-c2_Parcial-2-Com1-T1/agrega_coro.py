""" Definir una función, denominada “agrega_coro”, que reciba como parámetros una cadena
de caracteres (coro) que representa el nombre de un coro, un número (cant) que
representa su cantidad de integrantes y una lista (max_coros) compuesta por un número y
una lista de nombres de coros, y que devuelva como resultado la misma lista, con el
agregado “eventual” del nuevo coro, si es que el número cant coincide con el número que
es componente en la lista max_coros. [No es necesario validar los datos]
Ejemplo:  Dadas  la  cadena  'GCC'  el nro.  26  y la lista [ 26, [ 'GVD', 'Estudio Coral' ] ]
la función debería devolver  [ 26, [ 'GVD', 'Estudio Coral', 'GCC' ] ] """

def agrega_coro(cadena, numero, lista):
    if (numero == lista[0]):
        lista[1].append(cadena)
    return lista

cadena = 'GCC'
nro = 26
lista = [ 26, [ 'GVD', 'Estudio Coral' ] ]
print(agrega_coro(cadena, nro, lista))