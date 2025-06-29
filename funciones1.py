#Consigna: Crear una función que reciba una lista de números y devuelva una nueva lista con solo los números pares.

def filtrar_pares():
    numeros = input("Ingrese una lista de numeros separados por espacio: ")
    lista_numeros = [int(num) for num in numeros.split()]
    lista_pares = [num for num in lista_numeros if num % 2 == 0]
    return lista_pares
print(filtrar_pares())