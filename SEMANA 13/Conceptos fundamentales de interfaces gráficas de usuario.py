import tkinter as tk
from tkinter import messagebox

def agregar_texto():
    texto = entrada_texto.get()
    if texto:
        lista.insert(tk.END, texto)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

def limpiar_lista():
    lista.delete(0, tk.END)

#Crear ventana principal
ventana = tk.Tk()
ventana.title("Semana 13 - Charlie Cuaces")
ventana.geometry("300x300")

#Etiqueta
etiqueta = tk.Label(ventana, text="Escriba un texto:")
etiqueta.pack(pady=5)

#Campo de texto
entrada_texto = tk.Entry(ventana, width=30)
entrada_texto.pack(pady=5)

#Botón para agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_texto)
boton_agregar.pack(pady=5)

#Listbox para mostrar datos
lista = tk.Listbox(ventana, width=30, height=10)
lista.pack(pady=5)

#Botón para limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

#Ejecutar la aplicación
ventana.mainloop()
