import math
#  Crea un programa que analice texto y obtenga:
#  - Numero total de palabras.
#  - Longitud media de las palabras.
#  - Numero de oraciones del texto (cada vez que aparecen un punto).
#  - Encuentre la palabra mas larga.

def lista_palabras(texto : str):
    texto = texto.replace("."," ").replace(",", " ").replace(")","").replace("(","")
    return texto.lower().split()

def remover_puntos_y_coma(palabra):
    return palabra.replace("."," ").replace(",", " ")

def lista_oraciones(texto : str):
    frases = texto.split(".")
    frases_strip = []
    for frase in frases:
        frases_strip.append(frase.strip())
    return frases_strip

def mayor_longitud(lista : list[str]):
    mayor = 0
    for elemento in lista:
        if len(elemento) > mayor:
            mayor = len(elemento)
            valor = elemento
    return mayor, valor

def longitud_media_elementos(lista : list):
    cantidad_letras = 0
    for elemento in lista:
        cantidad_letras += len(elemento)
    return ((cantidad_letras)/(len(lista)))

def desafio_palabras(texto: str):
    palabras = lista_palabras(texto)
    oraciones = lista_oraciones(texto)
    print("Numero total de palabras:", len(palabras), "palabras.")
    print("Longitud media de las palabras:", f"{longitud_media_elementos(palabras):.2f}","caracteres.")
    print("Cantidad de oraciones:", len(oraciones), "oraciones.")
    cantidad_letras, palabra_mas_larga = mayor_longitud(palabras) 
    print(f"La palabra mas larga es '{palabra_mas_larga}' con {cantidad_letras} letras.")

texto = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencial igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.'
desafio_palabras(texto)

# palabras = texto.split()
# print("Mapeo con lambda:", list(map(lambda x: x.replace(",","").replace(".","").replace(")","").replace("(",""), palabras)))
# print("Mapeo con funcion:", list(map(remover_puntos_y_coma, palabras)))
# print("Filtro con lambda:", list(filter(lambda x: len(x) > 3, palabras)))
# print(palabras)