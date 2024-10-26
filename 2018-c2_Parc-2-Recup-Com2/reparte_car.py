""" Definir una función, denominada “reparte_car”, que reciba como parámetros una tupla (tup)
de  caracteres  y  una  cadena  (cad)  de  caracteres,  y  devuelva  como  resultado  una  tupla  de  dos
componentes, integrada por una cadena de caracteres y una lista. La cadena debe contener los
caracteres de tup que no están presentes en cad. La lista debe contener los caracteres de tup
que están presentes en cad, pero evitando repeticiones. [No es necesario validar los datos]
Ejemplos: Dada la tupla de caracteres  ('t', 'u', 'r', 'q', 'u', 'i', 'a')
    si la cadena de caracteres fuera  "devaluacion"
la función debería devolver la tupla  ('trq', ['u', 'i', 'a'])
    si la cadena de caracteres fuera  "desempleo"
la función debería devolver la tupla  ('turquia', [])
    si la cadena de caracteres fuera  "riesgo que fuga capitales"
la función debería devolver la tupla  ('',['t','u','r','q', 'i','a']) """

def reparte_car(tup, cad):
    cadena = ""
    lista = []
    # recorro la @tup
    for i in tup:
        # print(i)
        # cond. de si el elemento de @tup no esta en @cad y que no este en la cadena
        if (i not in cad and i not in cadena):
            cadena += i
        else:
            # cond. de si el elemento de @tup esta en @cad y que no este en la lista
            if (i in cad and i not in lista):
                lista.append(i)
    tupla = (cadena, lista)
    return tupla

tupla = ('t', 'u', 'r', 'q', 'u', 'i', 'a')
print(f'1er. LLamado: {reparte_car(tupla, cad="devaluacion")}')
print(f'2do. LLamado: {reparte_car(tupla, cad="desempleo")}')
print(f'3er. LLamado: {reparte_car(tupla, cad="riesgo que fuga capitales")}')