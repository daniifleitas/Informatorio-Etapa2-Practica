#Consigna: Pedir al usuario una lista de palabras separadas por espacio y mostrar cuántas palabras distintas hay (usá un conjunto).
palabras = input("Ingrese una lista de palabras separadas por espacio: ")
palabras = palabras.split()
palabras_distintas = set(palabras)
print("La cantidad de palabras distintas es: ", len(palabras_distintas))

