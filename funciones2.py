#Consigna: Crear una función que reciba una cadena de texto y devuelva un diccionario con cuántas veces aparece cada palabra.
def contar_palabras():
    texto = input("Ingrese una cadena de texto: ")
    texto = texto.split()
    diccionario_palabras = {}
    for palabra in texto:
        palabra = palabra.lower()
        if palabra in diccionario_palabras:
            diccionario_palabras[palabra] += 1
        else:
            diccionario_palabras[palabra] = 1
    return diccionario_palabras
print(contar_palabras())
