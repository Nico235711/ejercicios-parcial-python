""" Definir una función “encripta_frase”, que reciba como parámetros una cadena de
caracteres (cade) y un diccionario (donde cada clave sea una letra del abecedario y su
respectivo valor sea otra letra), y devuelva la cadena que resulta de sustituir en cade las
letras que sean clave en el diccionario, por sus respectivos valores. [No es necesario validar
los datos]
Ejemplo:   Dadas  la  cadena   '5to. semestre: faltan 35 dias'  y el diccionario
{ 'a' : "e", 'e' : "f", 'f' : "i" , 'i' : "l", 'l' : "n" , 'n' : "o" , 'o' : "r" , 'r' : "s" , 's' : " t" , 't' : "a" }
    la función debería devolver:  "5ar. tfmftasf: ienaeo 35 dlet"
"""

def encripta_frase(cade, diccionario):
    cadena = ""
    for i in cade:
        if (i in diccionario):
            cadena += diccionario[i]
        else:
            cadena += i
    return cadena

cadena = '5to. semestre: faltan 35 dias'
diccionario = { 'a' : "e", 'e' : "f", 'f' : "i" , 'i' : "l", 'l' : "n" , 'n' : "o" , 'o' : "r" , 'r' : "s" , 's' : "t" , 't' : "a" }
print(encripta_frase(cadena, diccionario))