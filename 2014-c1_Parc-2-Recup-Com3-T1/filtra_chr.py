""" Definir  una  función,  denominada  “filtra_chr”,  que  dados  como  parámetros  una  cadena  de
caracteres  binarios  (compuesta  por  unos  y  ceros)  y  una  cadena  de  texto,  ambas  de  igual
longitud,  devuelva  como  resultado  una  cadena  constituida  solamente  por  los  caracteres  del
texto  que  se  correspondan  (posicionalmente)  con  los  unos  de  la  cadena  binaria.  [No  es
necesario validar los datos.]
Ejemplo: Dados    filtro = “1011011011”      y      texto = "este texto"
la función debería devolver:   "eteteto" """

def filtra_chr(cadenaBinaria, texto):
    longitudCadenaBinaria = len(cadenaBinaria)
    if (longitudCadenaBinaria != len(texto)):
        return f"Las longitudes de {cadenaBinaria} y {texto} no son iguales"
    else:
        nuevoTexto = ""
        for numero in range(longitudCadenaBinaria):
            # cond. ternaria en python
            nuevoTexto += texto[numero] if (cadenaBinaria[numero] == "1") else ""
        return nuevoTexto

filtro = "1011011011"
texto = "este texto"
print(filtra_chr(filtro, texto))