#Consigna: Pedir al usuario que ingrese las notas de una materia (hasta que escriba fin) y luego mostrar el promedio.
while True:
    nota = input("Ingrese una nota y ponga 'fin' para terminar: ")
    if nota == "fin":
        break
    else:
        nota = float(nota)