import tkinter as tk
from tkinter import messagebox

# Añadir una tarea
def añadir_tarea():
    tarea = entrada_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor ingresar una tarea")

# Marcar una tarea completada
def marcar_completada():
    try:
        seleccion = lista_tareas.curselection()
        tarea = lista_tareas.get(seleccion)
        tarea_completada = f"[Completada] {tarea}"
        lista_tareas.delete(seleccion)
        lista_tareas.insert(seleccion, tarea_completada)
    except IndexError:
        messagebox.showwarning("Aviso", "Por favor seleccionar una tarea")

# Eliminar una tarea
def eliminar_tarea():
    try:
        seleccion = lista_tareas.curselection()
        lista_tareas.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Aviso", "Por favor selecciona una tarea")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Campo de entrada para añadir nuevas tareas
entrada_tarea = tk.Entry(ventana, width=50)
entrada_tarea.grid(row=0, column=0, padx=10, pady=10)

# Botón para añadir tareas
boton_anadir = tk.Button(ventana, text="Añadir Tarea", width=20, command=añadir_tarea)
boton_anadir.grid(row=0, column=1, padx=10, pady=10)

# Lista para mostrar las tareas
lista_tareas = tk.Listbox(ventana, width=50, height=10)
lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar una tarea como completada
boton_completada = tk.Button(ventana, text="Marcar como Completada", width=20, command=marcar_completada)
boton_completada.grid(row=2, column=0, padx=10, pady=10)

# Botón para eliminar una tarea
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", width=20, command=eliminar_tarea)
boton_eliminar.grid(row=2, column=1, padx=10, pady=10)

# Permitir añadir tarea presionando Enter
entrada_tarea.bind("<Return>", lambda event: añadir_tarea())
lista_tareas.bind('<c>', lambda event: marcar_completada())
lista_tareas.bind('<C>', lambda event: marcar_completada())
lista_tareas.bind('<d>', lambda event:eliminar_tarea())
lista_tareas.bind('<D>', lambda event:eliminar_tarea())
lista_tareas.bind('<Delete>', lambda event:eliminar_tarea())
lista_tareas.bind('<Escape>', lambda event: quit())

# Iniciar la aplicación
ventana.mainloop()
