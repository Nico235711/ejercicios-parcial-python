""" a. 1) Definir una función, denominada “mas_cortas”, que reciba como parámetros una cadena
(cad)  de  caracteres  y  una  tupla  (tup)  integrada  por  cadenas  de  caracteres,  y  devuelva  como
resultado  una  cadena  compuesta  con  la  concatenación  de  las  cadenas  de  la  tupla  tup  cuya
longitud sea inferior a la de la cadena cad. [No es necesario validar los datos]
Ejemplo: Dados la cadena "empleo" y  la tupla
('ver','piloto','de','drones','tambien','cerveza','artesanal')
la función debería devolver la cadena "verde"
2) Dar un ejemplo de invocación y utilización de “mas_cortas”, desde una función “main". """

def mas_cortas(cad, tup):
    cadena = ""
    for i in tup:
        # ternaria -> concanteno lo que valga i si la longitud de i es menor a la de @cad
        cadena += i if (len(i) < len(cad)) else ""
    return cadena

cadena = "empleo"
tupla = ('ver','piloto','de','drones','tambien','cerveza','artesanal')
print(mas_cortas(cadena, tupla))