#Consigna: Crear una función que reciba una lista y devuelva una nueva lista sin elementos repetidos, manteniendo el orden original.
def eliminar_repetidos():
    elementos = input("Ingrese una lista de elementos separados por espacio: ")
    lista_elementos = elementos.split()
    lista_sin_repetidos = []
    vistos = set()
    for elemento in lista_elementos:
        if elemento not in vistos:
            lista_sin_repetidos.append(elemento)
            vistos.add(elemento)
    return lista_sin_repetidos
print(eliminar_repetidos())