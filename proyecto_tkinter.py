import tkinter as tk
from tkinter import ttk

conversion_factores = {
    "Milímetro": 0.001,
    "Centímetro": 0.01,
    "Metro": 1,
    "Hectómetro": 100,
    "Kilómetro": 1000,
    "Pulgada": 0.0254,
    "Pies": 0.3048,
    "Milla": 1609.34
}

def convertir_unidades():
    try:
        valor = float(entry_valor.get())
        unidad_origen = definir_unidad_origen.get()
        unidad_destino = definir_unidad_destino.get()

        metros = valor * conversion_factores[unidad_origen]
        resultado = metros / conversion_factores[unidad_destino]
        label_resultado.config(text=f"{resultado:.2f} {unidad_destino}")
    except ValueError:
        label_resultado.config(text="Ingrese un número válido.")

ventana = tk.Tk()
ventana.title("Conversor de Unidades de métricas")
tk.Label(ventana, text="Valor:").grid(row=0, column=0, padx=100, pady=10)
entry_valor = tk.Entry(ventana)
entry_valor.grid(row=0, column=1, padx=5, pady=10)

tk.Label(ventana, text="Unidad de origen:").grid(row=1, column=0, padx=10, pady=10)
definir_unidad_origen = ttk.Combobox(ventana, values=list(conversion_factores.keys()))
definir_unidad_origen.grid(row=1, column=1, padx=10, pady=10)
tk.Label(ventana, text="Unidad de destino:").grid(row=2, column=0, padx=10, pady=10)
definir_unidad_destino = ttk.Combobox(ventana, values=list(conversion_factores.keys()))
definir_unidad_destino.grid(row=2, column=1, padx=10, pady=10)
tk.Button(ventana, text="Convertir", command=convertir_unidades).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
ventana.mainloop()