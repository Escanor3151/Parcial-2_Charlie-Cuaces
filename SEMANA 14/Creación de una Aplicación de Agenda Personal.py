import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
#Charlie Cuaces
def main():
    #Principal
    root = tk.Tk()
    root.title("Agenda Personal")
    root.geometry("500x400")
    #Frame
    frame_lista = tk.Frame(root)
    frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Etiqueta para la lista
    lbl_lista = tk.Label(frame_lista, text="Agenda Personal", font=("Arial", 12, "bold"))
    lbl_lista.pack(anchor='w')

    # Crear el Treeview
    columnas = ("Fecha", "Hora", "Descripcion")
    tree = ttk.Treeview(frame_lista, columns=columnas, show='headings', selectmode='browse')

    # Configurar columnas
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=70, anchor="center")

    # Scrollbar
    scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    #Frame de datos
    frame_form = tk.Frame(root)
    frame_form.pack(fill=tk.X, padx=10)

    # Etiqueta de Fecha
    lbl_fecha = tk.Label(frame_form, text="Fecha:")
    lbl_fecha.grid(row=0, column=0, padx=5, pady=5, sticky='e')
    entry_fecha = DateEntry(frame_form, width=12, background='turquoise', foreground='white', date_pattern='dd/mm/yyyy')
    entry_fecha.grid(row=0, column=1, padx=5, pady=5)

    # Etiqueta de la Hora
    lbl_hora = tk.Label(frame_form, text="Hora:")
    lbl_hora.grid(row=0, column=2, padx=5, pady=5, sticky='e')
    entry_hora = tk.Entry(frame_form, width=15)
    entry_hora.grid(row=0, column=3, padx=5, pady=5)

    # Etiqueta para la Descripción
    lbl_desc = tk.Label(frame_form, text="Descripcion:")
    lbl_desc.grid(row=1, column=0, padx=5, pady=5, sticky='e')
    entry_desc = tk.Entry(frame_form, width=35)
    entry_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

    #Frame de botones
    frame_botones = tk.Frame(root)
    frame_botones.pack(fill=tk.X, pady=10)

    # Función para agregar evento
    def agregar_evento():
        fecha = entry_fecha.get()
        hora = entry_hora.get()
        descripcion = entry_desc.get()

        if not hora or not descripcion:
            messagebox.showwarning("Incompleto", "Por favor llenar correctamente")
            return
        tree.insert("", tk.END, values=(fecha, hora, descripcion))
        # Limpiar
        entry_hora.delete(0, tk.END)
        entry_desc.delete(0, tk.END)

    # Funcion de eliminar
    def eliminar_evento():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleccion Vacia", "Por favor seleccione camp")
            return

        confirmar = messagebox.askyesno("Confirmar Eliminacion", "¿Estas seguro?")
        if confirmar:
            tree.delete(selected_item)

    # Botones
    btn_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_evento, bg='green', width=10)
    btn_agregar.pack(side=tk.LEFT, padx=10)

    btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_evento, bg='red', width=10)
    btn_eliminar.pack(side=tk.LEFT, padx=10)

    btn_salir = tk.Button(frame_botones, text="Salir", command=root.destroy, bg='pink', width=15)
    btn_salir.pack(side=tk.RIGHT, padx=10)

    # Ejecutar la aplicación
    root.mainloop()
# EjecuCION
if __name__ == "__main__":
    main()