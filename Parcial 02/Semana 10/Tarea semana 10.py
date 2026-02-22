#Jordan Muenala - 2026-02-22

# CLASE PRODUCTO

class Producto: # Clase para representar un producto en el inventario

    def __init__(self, id, nombre, cantidad, precio):  # Constructor para inicializar los atributos del producto
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # getters
    def get_id(self):  # Devuelve el ID del producto
        return self.id

    def get_nombre(self):  # Devuelve el nombre del producto
        return self.nombre

    def get_cantidad(self):  # Devuelve la cantidad del producto
        return self.cantidad

    def get_precio(self):  # Devuelve el precio del producto
        return self.precio

    # setters
    def set_cantidad(self, cantidad):  # Establece la cantidad del producto
        self.cantidad = cantidad

    def set_precio(self, precio):  # Establece el precio del producto
        self.precio = precio

    def __str__(self):  #
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"



# CLASE INVENTARIO

class Inventario:

    def __init__(self):  # Constructor para inicializar la lista de productos y cargar datos desde el archivo
        self.productos = []
        self.archivo = "inventario.txt"
        self.cargar_archivo()   # ← Cargar datos al iniciar



    # CARGAR DESDE ARCHIVO

    def cargar_archivo(self):  # Carga los productos desde un archivo de texto, creando objetos Producto y agregándolos a la lista
        try:  # Abrir el archivo en modo lectura
            with open(self.archivo, "r") as f:  # Leer cada línea del archivo
                for linea in f:  # Dividir la línea en partes usando la coma como separador
                    datos = linea.strip().split(",")

                    if len(datos) == 4:  # Verificar que la línea tenga los 4 campos necesarios
                        id = int(datos[0])
                        nombre = datos[1]
                        cantidad = int(datos[2])
                        precio = float(datos[3])

                        producto = Producto(id, nombre, cantidad, precio)
                        self.productos.append(producto)

            print("Inventario cargado desde archivo")

        except FileNotFoundError:  # Si el archivo no existe, se crea uno nuevo
            print("Archivo no existe, se creará uno nuevo")
            open(self.archivo, "w").close()

        except PermissionError:  # Si no hay permisos para leer el archivo, se muestra un mensaje de error
            print("No hay permisos para leer el archivo")



    # GUARDAR EN ARCHIVO

    def guardar_archivo(self):  # Guarda los productos en un archivo de texto, escribiendo cada producto en una línea con formato CSV (ID,Nombre,Cantidad,Precio)
        try:
            with open(self.archivo, "w") as f:  # Abrir el archivo en modo escritura (sobrescribe el contenido)
                for p in self.productos:  # Escribir cada producto en una línea con formato CSV
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    f.write(linea)

            print("Cambios guardados en archivo")

        except PermissionError:  # Si no hay permisos para escribir en el archivo, se muestra un mensaje de error
            print("No se pudo guardar el archivo (permiso denegado)")





    def agregar_producto(self, producto):  # Agrega un producto al inventario, verificando que el ID no exista previamente, y guarda automáticamente los cambios en el archivo
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("El ID ya existe")
                return

        self.productos.append(producto)  # Agrega el producto a la lista
        self.guardar_archivo()   # guardar automáticamente después de agregar
        print("Producto agregado y guardado")


    def eliminar_producto(self, id):  # Elimina un producto por su ID, y guarda automáticamente los cambios en el archivo
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                self.guardar_archivo()
                print("Producto eliminado y actualizado en archivo")
                return

        print("Producto no encontrado")


    def actualizar_producto(self, id, cantidad, precio):  # Actualiza cantidad y precio de un producto por su ID, y guarda automáticamente los cambios en el archivo
        for p in self.productos:
            if p.get_id() == id:
                p.set_cantidad(cantidad)
                p.set_precio(precio)
                self.guardar_archivo()
                print("Producto actualizado y guardado")
                return

        print("Producto no encontrado")


    def buscar_por_nombre(self, nombre):  # Busca productos por nombre (o parte del nombre), mostrando todas las coincidencias, o un mensaje si no se encuentran, sin modificar el archivo
        encontrados = False

        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                print(p)
                encontrados = True

        if not encontrados:  # Si no se encontraron coincidencias, se muestra un mensaje indicando que no hay resultados
            print("No hay coincidencias")


    def mostrar_todos(self):  # Muestra todos los productos en el inventario, o un mensaje si el inventario está vacío, sin modificar el archivo
        if not self.productos:
            print("Inventario vacío")
        else:
            for p in self.productos:
                print(p)



# MENÚ PRINCIPAL

def menu():
    inventario = Inventario()

    while True:
        print("\n====== INVENTARIO MINI SUPER TIA ======")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar por nombre")
        print("5. Mostrar todos")
        print("0. Salir")

        opcion = input("Seleccione opción: ")

        try:
            if opcion == "1":
                id = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            elif opcion == "2":
                id = int(input("ID a eliminar: "))
                inventario.eliminar_producto(id)

            elif opcion == "3":
                id = int(input("ID: "))
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(id, cantidad, precio)

            elif opcion == "4":
                nombre = input("Nombre a buscar: ")
                inventario.buscar_por_nombre(nombre)

            elif opcion == "5":
                inventario.mostrar_todos()

            elif opcion == "0":
                print("Saliendo del sistema...")
                break  # Salir del bucle y terminar el programa

            else:
                print("Opción inválida")

        except ValueError:  # Si el usuario ingresa un valor no numérico donde se espera un número, se captura la excepción y se muestra un mensaje de error
            print("Error: ingrese datos correctos (números donde corresponde)")


# Ejecutar programa
if __name__ == "__main__":  # Si este archivo se ejecuta directamente, se llama a la función
    menu()