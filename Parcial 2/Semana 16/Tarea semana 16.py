# Muenala Jordan_2026

import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Lista de tareas")
ventana.geometry("400x400",)
ventana.configure(bg="lightgray")
lista = tk.Listbox(ventana)

# Lista para guardar tareas
tareas = []

# Función para actualizar la lista visual
def actualizar_lista():
    lista.delete(0, tk.END)
    for tarea in tareas:
        texto = tarea["texto"]
        if tarea["completada"]:
            texto += " (Completada ✔)"
        lista.insert(tk.END, texto)

# Añadir tarea
def agregar_tarea(event=None):
    texto = entrada.get()
    if texto != "":
        tareas.append({"texto": texto, "completada": False})
        entrada.delete(0, tk.END)
        actualizar_lista()

# Marcar como completada
def completar_tarea(event=None):
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index]["completada"] = not tareas[index]["completada"]
        actualizar_lista()

# Eliminar tarea
def eliminar_tarea(event=None):
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas.pop(index)
        actualizar_lista()

# Cerrar aplicación
def cerrar(event=None):
    ventana.destroy()

# Widgets
entrada = tk.Entry(ventana, width=30, bg="black", fg="white")
entrada.pack(pady=10)

btn_agregar = tk.Button(ventana, text="Agregar tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(ventana, text="Completar tarea", command=completar_tarea)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

lista = tk.Listbox(ventana, width=40, height=10,bg="black", fg="white")
lista.pack(pady=10)

# foco a la lista
lista.focus_set()

# Atajos de teclado
ventana.bind("<Return>", agregar_tarea)
ventana.bind("<Escape>", cerrar)

# Atajos en la lista
lista.bind("c", completar_tarea)
lista.bind("d", eliminar_tarea)
lista.bind("<Delete>", eliminar_tarea)

# Doble clic para completar
lista.bind("<Double-Button-1>", completar_tarea)

# Ejecutar aplicación
ventana.mainloop()
