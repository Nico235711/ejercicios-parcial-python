""" Definir una función, denominada “reparte_letra”, que reciba como parámetro una cadena de
caracteres y devuelva como resultado una tupla compuesta por dos cadenas de caracteres:
la primera debe contener los caracteres que sean letras minúsculas, y la segunda cadena
debe contener los restantes caracteres, conservando el orden de aparición en ambas
(recordar que la función ord() de Python devuelve el valor 97 para la letra ‘a’ y 122 para la
letra ‘z’). [No es necesario validar los datos]
Ejemplo:   Dada    la  cadena    "#e2sla01cla6v@e"
la función debería devolver    ( 'eslaclave' , '#2016@' ) """

def reparte_letra(cadena):
    caracteresEspeciales = ""
    caracteres = ""
    for i in cadena:
        if (ord(i) >= 67 and ord(i) <= 122):
            caracteres += i
        else:
            caracteresEspeciales += i
    return (caracteres, caracteresEspeciales)

cadena = "#e2sla01cla6v@e"
print(reparte_letra(cadena))