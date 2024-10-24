""" Definir una función, denominada "cuantas_veces", que dados como parámetros dos cadenas
de caracteres (integradas por letras y espacios), devuelva como resultado la cantidad de veces
que la primera cadena se encuentra contenida "exactamente" en la segunda. [No es necesario
validar los datos, ni considerar mayúsculas.]
Ejemplos:   Dados   cade = "ente"    y   cadena = "no se lamente la mente inteligente"
la función debería devolver el valor   3
Si fuera  cade = "ante"  entonces la función debería devolver el valor   0 """

def cuantas_veces(cade, cadena):
    resultado = 0
    longitudCade = len(cade)
    longitudCadena = len(cadena)
    for i in range(longitudCadena):
        # cadena[i:i + longitudCade] -> slicing toma una subcadena de igual longitud que @cade
        # print(f"cadena[i + longitudCade + 1]: {cadena[i + longitudCade + 1]}") se sale del rango

        # print(f"cadena[i:longitudCade]: {cadena[i:longitudCade]}") el punto final es indenpendiente del i

        if (cade == cadena[i:i + longitudCade]):
            # print(f"cadena[i:i + longitudCade]: {cadena[i:i + longitudCade]}")
            resultado += 1
    return resultado

# Solo se ejecuta si este archivo se ejecuta directamente
if __name__ == "__main__":
        cade = "ente"
        cadena = "no se lamente la mente inteligente"
        texto = "vez" if (cuantas_veces(cade, cadena) == 1) else "veces"
        mensaje = f"{cade} no se encuentra en {cadena}" if (cuantas_veces(cade, cadena) == 0) else f"'{cade}' se encuentra exactamente {cuantas_veces(cade, cadena)} {texto} en '{cadena}'"

        print(mensaje)

        cade = "ante"
        cadena = "no se lamente la mente inteligente"
        mensaje = f"'{cade}' no se encuentra en '{cadena}'" if (cuantas_veces(cade, cadena) == 0) else f"'{cade}' se encuentra exactamente {cuantas_veces(cade, cadena)} {texto} en '{cadena}'"

        print(mensaje)