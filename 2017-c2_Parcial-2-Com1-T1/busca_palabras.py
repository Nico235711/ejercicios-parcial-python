""" Definir una función, denominada “busca_palabras”, que reciba como parámetros un
carácter (car) y una tupla de cadenas, cada una de las cuales representa una palabra, y
que devuelva la cadena que resulta de concatenar todas aquellas palabras de la tupla que
contengan el carácter car. [No es necesario validar los datos]
Ejemplo:
Dados el carácter  "n"
y la tupla  ('existe', "una", "cadena", "especial", "que", "no", "contiene", "caracteres")
la función debería devolver "unacadenanocontiene" """

def busca_palabras(car, tupla):
    cadena = ""
    for i in tupla:
        if (car in i):
            cadena += i
    return cadena

caracter = "n"
tupla = ('existe', "una", "cadena", "especial", "que", "no", "contiene", "caracteres")
print(busca_palabras(caracter, tupla))