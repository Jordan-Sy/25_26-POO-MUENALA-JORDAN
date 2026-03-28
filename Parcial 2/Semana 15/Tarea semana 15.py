#Jordan Muenala 2026

import tkinter as tk

# ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("500x400")
ventana.configure(bg="lightblue")

# funciones

def agregar_tarea(event=None):  # event para poder usar Enter
    tarea = entrada.get()

    if tarea != "":
        lista.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
    else:
        print("No escribiste nada")


def completar_tarea():
    try:
        indice = lista.curselection()[0]
        texto = lista.get(indice)

        # marcar como completada
        lista.delete(indice)
        if "(hecho)" not in texto:
            lista.insert(indice, texto + " (hecho)")
        else:
            lista.insert(indice, texto.replace(" (hecho)", ""))
    except:
        print("Selecciona una tarea")


def eliminar_tarea():
    try:
        indice = lista.curselection()[0]
        lista.delete(indice)
    except:
        print("Selecciona una tarea para eliminar")


# interfaz

entrada = tk.Entry(ventana, width=30 , bg="white", fg="black")
entrada.pack(pady=10)

# evento con Enter
entrada.bind("<Return>", agregar_tarea)

boton_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

boton_completar = tk.Button(ventana, text="Marcar como Completada", command=completar_tarea)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

lista = tk.Listbox(ventana, width=40, height=10, bg="black", fg="white")
lista.pack(pady=10)


# opcional: doble clic para completar
def doble_click(event):
    completar_tarea()


lista.bind("<Double-Button-1>", doble_click)

# iniciar app
ventana.mainloop()