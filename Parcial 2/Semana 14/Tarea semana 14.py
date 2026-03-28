# Jordan Muenala 2026
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# intento de clase
class Agenda:

    def __init__(self, root):
        self.root = root
        self.root.title("Mi Agenda xd")

        # lista donde guardo cosas
        self.eventos = []

        # FRAME 1 (lista)
        self.frame1 = tk.Frame(root)
        self.frame1.pack()

        self.tree = ttk.Treeview(self.frame1, columns=("Fecha", "Hora", "Desc"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Desc", text="Descripcion")
        self.tree.pack()

        # FRAME 2 (inputs)
        self.frame2 = tk.Frame(root)
        self.frame2.pack()

        tk.Label(self.frame2, text="Fecha").grid(row=0, column=0)
        self.entry_fecha = tk.Entry(self.frame2)
        self.entry_fecha.grid(row=0, column=1)

        tk.Label(self.frame2, text="Hora").grid(row=1, column=0)
        self.entry_hora = tk.Entry(self.frame2)
        self.entry_hora.grid(row=1, column=1)

        tk.Label(self.frame2, text="Descripcion").grid(row=2, column=0)
        self.entry_desc = tk.Entry(self.frame2)
        self.entry_desc.grid(row=2, column=1)

        # FRAME 3 (botones)
        self.frame3 = tk.Frame(root)
        self.frame3.pack()

        self.btn_add = tk.Button(self.frame3, text="Agregar Evento", command=self.agregar)
        self.btn_add.grid(row=0, column=0)

        self.btn_delete = tk.Button(self.frame3, text="Eliminar Evento", command=self.eliminar)
        self.btn_delete.grid(row=0, column=1)

        self.btn_salir = tk.Button(self.frame3, text="Salir", command=root.quit)
        self.btn_salir.grid(row=0, column=2)

    # funcion agregar
    def agregar(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        desc = self.entry_desc.get()

        # no valido
        if fecha == "" or hora == "" or desc == "":
            messagebox.showwarning("Error", "Llena todo pls")
            return

        # guardo en lista
        self.eventos.append((fecha, hora, desc))

        # inserto en tabla
        self.tree.insert("", "end", values=(fecha, hora, desc))

        # limpio campos
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    def eliminar(self):
        seleccionado = self.tree.selection()

        # si no selecciona nada
        if seleccionado == ():
            messagebox.showinfo("Info", "Selecciona algo primero")
            return

        # confirmacion
        resp = messagebox.askyesno("Seguro?", "Quieres borrar esto?")
        if resp:
            for item in seleccionado:
                self.tree.delete(item)
                # no elimino de la lista eventos (error leve xd)

# main
root = tk.Tk()
app = Agenda(root)
root.mainloop()