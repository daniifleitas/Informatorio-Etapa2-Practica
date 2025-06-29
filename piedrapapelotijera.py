import tkinter as tk
import random

def jugar(eleccion_usuario):
    opciones = ['Piedra', 'Papel', 'Tijera']
    eleccion_computadora = random.choice(opciones)

    label_usuario.config(text=f"Elegiste: {eleccion_usuario}")
    label_computadora.config(text=f"Computadora eligió: {eleccion_computadora}")
    
    if eleccion_usuario == eleccion_computadora:
        resultado = "¡Empate!"
    elif (eleccion_usuario == 'Piedra' and eleccion_computadora == 'Tijera') or \
        (eleccion_usuario == 'Papel' and eleccion_computadora == 'Piedra') or \
        (eleccion_usuario == 'Tijera' and eleccion_computadora == 'Papel'):
        resultado = "¡Ganaste!"
    else:
        resultado = "¡Perdiste!"
        
    label_resultado.config(text=resultado)



ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.configure(bg="#f7d5f8") 
ventana.geometry("300x300")


boton_piedra = tk.Button(ventana, text="Piedra", font=("Arial", 12), bg="#f7d5f8", width=15, command=lambda: jugar('Piedra'))
boton_papel = tk.Button(ventana, text="Papel", font=("Arial", 12), bg="#f7d5f8", width=15, command=lambda: jugar('Papel'))
boton_tijera = tk.Button(ventana, text="Tijera", font=("Arial", 12), bg="#f7d5f8", width=15, command=lambda: jugar('Tijera'))

boton_piedra.pack(pady=5)
boton_papel.pack(pady=5)
boton_tijera.pack(pady=5)


label_usuario = tk.Label(ventana, text="Elegiste: ", font=("Arial", 12), bg="#f7d5f8")
label_usuario.pack(pady=10)

label_computadora = tk.Label(ventana, text="Computadora eligió: ", font=("Arial", 12), bg="#f7d5f8")
label_computadora.pack(pady=10)

label_resultado = tk.Label(ventana, text="¿Quién ganará?", font=('Arial', 14, 'bold'), bg="#f7d5f8")
label_resultado.pack(pady=10)

ventana.mainloop()