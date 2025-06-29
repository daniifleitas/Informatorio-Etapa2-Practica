#Consigna: Pedir al usuario 5 números y almacenarlos en una lista. Luego mostrar la lista en orden inverso.
print("Ingrese 5 numeros:")
num_1 = int(input("Numero 1: "))
num_2 = int(input("Numero 2: "))
num_3 = int(input("Numero 3: "))
num_4 = int(input("Numero 4: "))
num_5 = int(input("Numero 5: "))
numeros = [num_1, num_2, num_3, num_4, num_5]
print("Lista en orden inverso: ", numeros[::-1])
