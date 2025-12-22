# Clase Producto
class Producto: # Representa un producto con nombre y precio

    def __init__(self, nombre, precio): # Inicializa el producto con nombre y precio
        self.nombre = nombre
        self.precio = precio


# Clase Cliente
class Cliente: # Representa un cliente con un nombre

    def __init__(self, nombre):
        self.nombre = nombre


# Clase Carrito de compras
class Carrito: # Representa un carrito de compras asociado a un cliente

    def __init__(self, cliente):# Inicializa el carrito con un cliente y una lista vacía de productos
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, producto): # Agrega un producto al carrito
        self.productos.append(producto)
        print(f"{producto.nombre} agregado al carrito de {self.cliente.nombre}.")

    def total(self): # Calcula el total de la compra en el carrito
        total = 0
        for producto in self.productos: # Itera sobre los productos en el carrito
            total += producto.precio
        return total # Retorna el total acumulado


# ------------------ Ejemplo de uso ------------------

# Crear productos
manzana = Producto("Manzana", 0.5)
pan = Producto("Pan", 1.2)
leche = Producto("Leche", 1.5)

# Crear un cliente
cliente1 = Cliente("Edwin")

# Crear un carrito para el cliente
carrito1 = Carrito(cliente1)

# Agregar productos al carrito
carrito1.agregar_producto(manzana)
carrito1.agregar_producto(pan)
carrito1.agregar_producto(leche)

# Mostrar total de la compra
print(f"\nTotal a pagar por {cliente1.nombre}: ${carrito1.total():.2f}")

