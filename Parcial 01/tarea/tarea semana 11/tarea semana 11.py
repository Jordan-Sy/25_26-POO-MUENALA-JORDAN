class Inventario:

    def __init__(self):
        self.productos = {}
        self.archivo = "inventario.txt"
        self.cargar_archivo()


    # ------------------
    # cargar
    # ------------------
    def cargar_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    id, nombre, cantidad, precio = linea.strip().split(",")

                    producto = Producto(
                        int(id),
                        nombre,
                        int(cantidad),
                        float(precio)
                    )

                    self.productos[producto.get_id()] = producto

            print("Inventario cargado correctamente")

        except FileNotFoundError:
            open(self.archivo, "w").close()

        except Exception as e:
            print("Error cargando:", e)


    # ------------------
    # guardar
    # ------------------
    def guardar_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos.values():
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")

        except Exception as e:
            print("Error guardando:", e)


    # ------------------
    # agregar
    # ------------------
    def agregar_producto(self, producto):

        if producto.get_id() in self.productos:
            print("El ID ya existe")
            return

        if producto.get_cantidad() < 0 or producto.get_precio() < 0:
            print("Cantidad o precio inválidos")
            return

        self.productos[producto.get_id()] = producto
        self.guardar_archivo()
        print("Producto agregado")


    # ------------------
    # eliminar
    # ------------------
    def eliminar_producto(self, id):

        if id not in self.productos:
            print("No encontrado")
            return

        del self.productos[id]
        self.guardar_archivo()
        print("Producto eliminado")


    # ------------------
    # actualizar
    # ------------------
    def actualizar_producto(self, id, cantidad, precio):

        if id not in self.productos:
            print("No encontrado")
            return

        if cantidad < 0 or precio < 0:
            print("Valores inválidos")
            return

        p = self.productos[id]
        p.set_cantidad(cantidad)
        p.set_precio(precio)

        self.guardar_archivo()
        print("Actualizado")


    # ------------------
    # buscar
    # ------------------
    def buscar_por_nombre(self, nombre):

        encontrados = [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

        if not encontrados:
            print("Sin coincidencias")
        else:
            for p in encontrados:
                print(p)


    # ------------------
    # mostrar
    # ------------------
    def mostrar_todos(self):

        if not self.productos:
            print("Inventario vacío")
            return

        for p in sorted(self.productos.values(), key=lambda x: x.get_id()):
            print(p)