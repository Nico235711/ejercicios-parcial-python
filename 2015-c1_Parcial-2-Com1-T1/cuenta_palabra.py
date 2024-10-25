""" Definir una función, denominada "cuenta_palabra", que reciba como parámetros una tupla
(compuesta por palabras sin repetición) y una lista de cadenas de caracteres (que contiene
todas los palabras de la tupla), y devuelva como resultado un diccionario, en donde las
claves sean cada una de los palabras de la tupla, y cada valor, la cantidad de apariciones
en las que la palabra ocurre en la lista de cadenas. [No es necesario validar los datos.]
Ejemplo:   Dadas  la  tupla = ("de", "el", "es")  y  la  lista = [ "el", "es", "el", "de", "siempre"]
la función debería devolver (en cualquier orden)
{ 'de' : 1 ,  'el' : 2 , 'es' : 1 } """

def cuenta_palabra(tupla, lista):
    diccionario = {}
    for i in tupla:
        if (i not in diccionario and i in lista):
            # .count() cuenta las veces que aparece el elemento en la lista
            diccionario[i] = lista.count(i)
    return diccionario

tupla = ("de", "el", "es")
lista = [ "el", "es", "el", "de", "siempre"]
print(cuenta_palabra(tupla, lista))