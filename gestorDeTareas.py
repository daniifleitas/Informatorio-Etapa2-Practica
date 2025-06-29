import tkinter as tk
from tkinter import messagebox
from datetime import datetime

tareas = []

# Función de reloj
def mostrar_reloj():
    hora_actual = datetime.now().strftime("%H:%M:%S")
    etiqueta_reloj.config(text=hora_actual)
    etiqueta_reloj.after(1000, mostrar_reloj)

# Función para marcar tarea como completada
def completar_tarea(texto_label):
    texto_label.config(fg="gray", font=("Arial", 10, "overstrike"))

def eliminar_tarea(tarea):
    if tarea in tareas:
        tareas.remove(tarea)
        mostrar_tareas()

# Función para agregar tareas a la lista
def agregar_tarea():
    texto = entrada_tarea.get()
    if texto:
        tareas.append(texto)
        mostrar_tareas()
        tareas == ""
        messagebox.showinfo("Tarea agregada", f"La tarea ha sido agregada.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

# Función para mostrar tareas en la interfaz
def mostrar_tareas():
    
    for widget in marco_tareas.winfo_children():
        widget.destroy()

    for tarea in tareas:
        tarea_frame = tk.Frame(marco_tareas, bg="#ffffff", pady=2)
        tarea_frame.pack(fill="x", padx=5, pady=2)

        texto_label = tk.Label(tarea_frame, text=tarea, font=("Arial", 10), bg="#ffffff", anchor="w")
        texto_label.pack(side="left", padx=5, fill="x", expand=True)

        boton_check = tk.Button(
            tarea_frame,
            text="✓",
            command=lambda l=texto_label: completar_tarea(l),
            bg="#c0f0c0",
            font=("Arial", 10, "bold")
        )
        boton_check.pack(side="right", padx=5)

        boton_eliminar = tk.Button(tarea_frame, text="🗑", 
            command=lambda t=tarea: eliminar_tarea(t), 
            bg="#f5a3a3", 
            font=("Arial", 10)
        )
        boton_eliminar.pack(side="right", padx=2)

# TKINTER
ventana = tk.Tk()
ventana.title("Gestor de tareas")
ventana.geometry("600x400")
ventana.configure(bg="#edd9ee")
ventana.resizable(True, False)

# Reloj
etiqueta_reloj = tk.Label(ventana, font=("Arial", 12), fg="black", bg="#edd9ee")
etiqueta_reloj.pack(anchor="ne", padx=10, pady=5)
mostrar_reloj()

# Entrada de tareas
entrada_texto = tk.Label(ventana, text="Ingrese una tarea:", font=("Arial", 10), bg="#edd9ee")
entrada_texto.pack(pady=5)
entrada_tarea = tk.Entry(ventana, font=("Arial", 10), width=30)
entrada_tarea.pack(pady=5)
boton_agregar = tk.Button(ventana, text="Agregar tarea", command=agregar_tarea, font=("Arial", 10), bg="#f0b3c6")
boton_agregar.pack(pady=5)

# Marco donde se mostrarán las tareas
marco_tareas = tk.Frame(ventana, bg="#edd9ee")
marco_tareas.pack(fill="both", expand=True, padx=10, pady=10)

#Scroll

contenedor_canvas = tk.Frame(ventana, bg="#edd9ee")
contenedor_canvas.pack(fill="both", expand=True, padx=10, pady=10)

canvas = tk.Canvas(contenedor_canvas, bg="#edd9ee", highlightthickness=0)
scrollbar = tk.Scrollbar(contenedor_canvas, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Frame interno dentro del canvas
marco_tareas = tk.Frame(canvas, bg="#edd9ee")
canvas.create_window((0, 0), window=marco_tareas, anchor="nw", width=canvas.winfo_reqwidth())

# Ajustar scroll automáticamente
def actualizar_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

marco_tareas.bind("<Configure>", actualizar_scroll)

# Para que no se encojan las tareas al hacer scroll
def ajustar_ancho(event):
    canvas.itemconfig("marco_tareas", width=event.width)

canvas.bind("<Configure>", lambda e: canvas.itemconfig(canvas.find_withtag("marco_tareas"), width=e.width))

canvas.create_window((0, 0), window=marco_tareas, anchor="nw", tags="marco_tareas")

ventana.mainloop()