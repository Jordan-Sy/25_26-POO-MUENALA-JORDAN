#Jordan Muenala - 2026-02-15
# CLASE PRODUCTO

class Producto:  # Clase para representar un producto en el inventario

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

    def __str__(self):  # Metodo especial para representar el producto como una cadena de texto
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"


# =========================
# CLASE INVENTARIO
# =========================
class Inventario:  # Clase para gestionar el inventario de productos

    def __init__(self):  # Constructor para inicializar la lista de productos
        self.productos = []  # Lista para almacenar objetos Producto

    # Añadir producto
    def agregar_producto(self, producto): # Agrega un producto al inventario, verificando que el ID no exista previamente
        for p in self.productos:
            if p.get_id() == producto.get_id():  # Verificar que el ID no exista
                print("El ID ya existe")
                return
        self.productos.append(producto)  # Agrega el producto a la lista
        print("Producto agregado")

    # Eliminar
    def eliminar_producto(self, id):  # Elimina un producto por su ID
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print("Producto eliminado")
                return
        print("Producto no encontrado")

    # Actualizar
    def actualizar_producto(self, id, cantidad, precio):  # Actualiza cantidad y precio de un producto por su ID
        for p in self.productos:
            if p.get_id() == id:
                p.set_cantidad(cantidad)
                p.set_precio(precio)
                print("Producto actualizado")
                return
        print("Producto no encontrado")

    # Buscar por nombre
    def buscar_por_nombre(self, nombre): # Busca productos por nombre
        encontrados = False
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower(): # Ignora si son mayúsculas o minúsculas
                print(p)
                encontrados = True

        if not encontrados:
            print("No hay coincidencias")

    # Mostrar todos
    def mostrar_todos(self):  # Muestra todos los productos en el inventario
        if not self.productos:
            print("Inventario vacío")
        else:
            for p in self.productos:
                print(p)


# =========================
# MENÚ PRINCIPAL
# =========================
def menu():
    inventario = Inventario()  # Crear una instancia de Inventario para gestionar los productos

    while True:
        print("\n====== INVENTARIO MINI SUPER TIA ======")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar por nombre")
        print("5. Mostrar todos")
        print("0. Salir")

        opcion = input("Seleccione opción: ")

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
            break

        else:
            print("Opción inválida")


# Ejecutar programa
if __name__ == "__main__":
    menu()
