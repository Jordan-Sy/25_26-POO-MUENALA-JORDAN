class Telefono: # Clase que representa un telefono movil
    def __init__(self, marca, modelo, color, almacenamiento, ram): # Inicializa el telefono con sus atributos
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.almacenamiento = almacenamiento  # en GB
        self.ram = ram  # en GB

    def obtener_info(self): # Retorna la informacion del telefono
        return (f"Telefono Info:\n"
                f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Color: {self.color}\n"
                f"Almacenamiento: {self.almacenamiento}GB\n"
                f"RAM: {self.ram}GB")

    def llamar(self, numero): # Simula hacer una llamada a un numero
        return f"Llamando al {numero} desde el {self.marca} {self.modelo}." # Retorna el string de la llamada

    def enviar_mensaje(self, numero, mensaje): # Simula enviar un mensaje a un numero
        return f"Enviando mensaje to {numero}: {mensaje}" # Retorna el string del mensaje enviado


# Ejemplo de creacion y uso de un objeto Telefono
telefono1 = Telefono("Samsung", "Galaxy", "Negro", 128, 6)
print(telefono1.obtener_info())
print(telefono1.llamar("123456789"))
print(telefono1.enviar_mensaje("123456789", "Hola, ¿cómo estás ?"))
