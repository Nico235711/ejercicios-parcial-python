""" Definir una función, denominada “actualiza_prec”, que reciba como parámetros un
diccionario (con artículos como clave y su respectivo precio como valor) y una lista de tuplas
(de  dos  componentes  cada  una,  la  primera  representa  un  artículo  y  la  segunda  su  nuevo
precio), y devuelva como resultado una lista con las tuplas cuya actualización en el
diccionario fracase. La función deberá modificar el diccionario con los precios actualizados.
[No es necesario validar los datos]
Ejemplo: Dados la lista [("oj",300), ("kmisa",700), ("kfe",130), ("t",20)] 
    y el diccionario  {'kmisa': 500, 'oj': 250, 'pan': 60, 't': 18} la función debería actualizar el diccionario de modo que quede
{'kmisa': 700, 'oj': 300, 'pan': 60, 't': 20} y devolver la lista    [('kfe', 130)]"""

def actualiza_prec(diccionario, lista):
    lista_nueva = []
    for i in lista:
        if (i[0] in diccionario):
            diccionario[i[0]] = i[1]
        else:
            lista_nueva.append(i)
    return lista_nueva

lista = [("oj",300), ("kmisa",700), ("kfe",130), ("t",20)] 
diccionario = {'kmisa': 500, 'oj': 250, 'pan': 60, 't': 18}
print(f"El precio que fallo en actualizarse en el diccionario fue {actualiza_prec(diccionario, lista)}")
print(f"El diccionario actualizado es {diccionario}")