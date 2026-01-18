# Programa: Personajes de terror
# Descripción:
# Este programa demuestra el uso de Programación Orientada a Objetos aplicando herencia, encapsulación y polimorfismo en Python.


class PersonajeTerror:  # Clase base que representa un personaje de una historia de terror.


    def __init__(self, nombre, nivel_miedo):  #Constructor de la clase base
        self.nombre = nombre
        # Encapsulación: atributo privado
        self.__nivel_miedo = nivel_miedo

    def obtener_nivel_miedo(self):  # Método para acceder al atributo privado

        # Devuelve el nivel de miedo del personaje.

        return self.__nivel_miedo

    def aumentar_miedo(self):  # Método para modificar el atributo privado

        # Aumenta el nivel de miedo del personaje.

        self.__nivel_miedo += 5
        print(f"{self.nombre} aumenta el miedo. Nivel actual: {self.__nivel_miedo}")

    def aparecer(self):  # Método que será sobrescrito por las clases hijas

        print(f"{self.nombre} aparece de manera misteriosa.")


class Fantasma(PersonajeTerror): # Clase derivada que representa un fantasma.


    def __init__(self, nombre, nivel_miedo, lugar):  #Constructor de la clase derivada
        super().__init__(nombre, nivel_miedo)
        self.lugar = lugar

    def aparecer(self):  # Método sobrescrito (Polimorfismo: comportamiento específico del fantasma.)

        print(f"{self.nombre} susurra en el {self.lugar}, causando escalofríos.")


class HombreLobo(PersonajeTerror):  # Clase derivada que representa un hombre lobo.


    def __init__(self, nombre, nivel_miedo, fase_lunar):  #Constructor de la clase derivada
        super().__init__(nombre, nivel_miedo)
        self.fase_lunar = fase_lunar

    def aparecer(self): # Método sobrescrito ( Polimorfismo: comportamiento específico del hombre lobo.)

        if self.fase_lunar == "Luna llena":
            print(f"{self.nombre} aúlla con furia bajo la luna llena.")
        else:
            print(f"{self.nombre} se oculta esperando la luna llena.")


# Programa principal
if __name__ == "__main__":  # Punto de entrada del programa
    # Creación de objetos
    fantasma = Fantasma("Gasparin", 40, "pasillo abandonado")
    hombre_lobo = HombreLobo("Remus Lupin", 60, "Luna llena")

    # Polimorfismo
    fantasma.aparecer()
    hombre_lobo.aparecer()

    # Encapsulación: acceso mediante método
    print("Nivel de miedo del fantasma:", fantasma.obtener_nivel_miedo())
    print("Nivel de miedo del hombre lobo:", hombre_lobo.obtener_nivel_miedo())

    # Modificación del atributo encapsulado
    fantasma.aumentar_miedo()
    hombre_lobo.aumentar_miedo()
