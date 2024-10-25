""" Definir  una  función  “detalle_longitudes”,  que  reciba  como  parámetro  una  tupla  compuesta
por cadenas de caracteres que representan palabras, y devuelva como resultado un diccionario
en donde las claves sean las longitudes de esas palabras, y los valores, la lista respectiva con
las palabras que tienen esa longitud. [No es necesario validar los datos.]
Ejemplo:   Dada  la  tupla = (' no', 'se', 'lamente', 'la', 'mente', 'inteligente ')
la función debería devolver (en cualquier orden)
{ 2 : ['no', 'se', 'la'] , 11: ['inteligente'] , 5 : ['mente'] , 7 : ['lamente'] } """

def detalle_longitudes(tupla):
    diccionarioLongitudes = {}
    for i in tupla:
        # print(i)
        longitud = len(i)
        if (longitud not in diccionarioLongitudes):
            diccionarioLongitudes[longitud] = [i]
        else:
            diccionarioLongitudes[longitud].append(i)
    print(f"{diccionarioLongitudes}")

tupla = ('no', 'se', 'lamente', 'la', 'mente', 'inteligente')
detalle_longitudes(tupla)