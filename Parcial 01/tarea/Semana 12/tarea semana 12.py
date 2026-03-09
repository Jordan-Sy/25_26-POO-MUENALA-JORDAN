# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable con titulo y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} ({self.categoria}) - ISBN: {self.isbn}"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario ISBN -> Libro
        self.usuarios = set()  # Conjunto de IDs de usuario
        self.historial_prestamos = {}  # ID usuario -> lista de ISBN

    # Añadir un libro
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' agregado.")

    # Quitar un libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro '{libro.info[0]}' eliminado.")
        else:
            print("Libro no encontrado.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print("El usuario ya existe.")
        else:
            self.usuarios.add(usuario.id_usuario)
            self.historial_prestamos[usuario.id_usuario] = []
            print(f"Usuario '{usuario.nombre}' registrado.")

    # Dar de baja usuario
    def baja_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            self.usuarios.remove(usuario.id_usuario)
            self.historial_prestamos.pop(usuario.id_usuario, None)
            print(f"Usuario '{usuario.nombre}' dado de baja.")
        else:
            print("Usuario no encontrado.")

    # Prestar libro
    def prestar_libro(self, isbn, usuario):
        if isbn not in self.libros:
            print("Libro no disponible.")
            return
        if usuario.id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario.libros_prestados.append(self.libros[isbn])
        self.historial_prestamos[usuario.id_usuario].append(isbn)
        print(f"Libro '{self.libros[isbn].info[0]}' prestado a {usuario.nombre}.")
        # Opcional: quitar libro de disponibilidad
        # self.libros.pop(isbn)

    # Devolver libro
    def devolver_libro(self, isbn, usuario):
        encontrado = False
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                encontrado = True
                print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
                break
        if not encontrado:
            print("El usuario no tiene este libro prestado.")

    # Buscar libros por título, autor o categoría
    def buscar_libro(self, busqueda):
        resultados = []
        for libro in self.libros.values():
            if busqueda.lower() in libro.info[0].lower() or busqueda.lower() in libro.info[1].lower() or busqueda.lower() in libro.categoria.lower():
                resultados.append(libro)
        if resultados:
            print("Resultados de búsqueda:")
            for l in resultados:
                print(l)
        else:
            print("No se encontraron libros.")

    # Listar libros prestados a un usuario
    def listar_prestados(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        if not usuario.libros_prestados:
            print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)


# ------------------------------
# Ejemplo de uso (pruebas)
# ------------------------------
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "111")
libro2 = Libro("Python Básico", "Juan Pérez", "Programación", "222")
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "333")

usuario1 = Usuario("Kevin", 1)
usuario2 = Usuario("Ana", 2)

biblioteca = Biblioteca()

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("111", usuario1)
biblioteca.prestar_libro("222", usuario1)
biblioteca.prestar_libro("333", usuario2)

# Listar libros prestados
biblioteca.listar_prestados(usuario1)
biblioteca.listar_prestados(usuario2)

# Buscar libros
biblioteca.buscar_libro("python")
biblioteca.buscar_libro("novela")

# Devolver libros
biblioteca.devolver_libro("222", usuario1)
biblioteca.listar_prestados(usuario1)