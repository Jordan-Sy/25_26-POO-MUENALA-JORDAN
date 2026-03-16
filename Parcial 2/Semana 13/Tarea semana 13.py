import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos")

# Funciones
def agregar_dato():
    texto = entrada.get()  # Obtener texto del campo
    if texto != "":
        lista.insert(tk.END, texto)  # Agregar a la lista
        entrada.delete(0, tk.END)  # Limpiar campo

def limpiar_lista():
    lista.delete(0, tk.END)  # Borrar todos los datos

# Componentes GUI
# Etiqueta
label = tk.Label(ventana, text="Ingrese un nombre:")
label.pack()

# Campo de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Botón agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack()

# Botón limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack()

# Lista para mostrar datos
lista = tk.Listbox(ventana)
lista.pack()

# Ejecutar ventana
ventana.mainloop()