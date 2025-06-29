#Consigna: Crear un diccionario que contenga nombres de productos como claves y cantidades como valores. Luego permitir al usuario actualizar existencias o agregar nuevos productos, hasta que escriba salir.
diccionario = {"manzanas": 10, "naranjas": 5, "peras": 8}
while True:
    producto = input("Ingrese el nombre del producto o 'salir' para terminar: ")
    if producto == "salir":
        break
    else: 
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if producto in diccionario:
            diccionario[producto] += cantidad
        else:
            diccionario[producto] = cantidad
print("Inventario actualizado: ", diccionario)
