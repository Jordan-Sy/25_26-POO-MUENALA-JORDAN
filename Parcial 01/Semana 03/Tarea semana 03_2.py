class ClimaDia: # Clase para representar el clima de un día
    def __init__(self, temperatura): # Constructor que recibe la temperatura
        # Encapsulamiento: atributo "protegido"
        self._temperatura = temperatura # Atributo para almacenar la temperatura

    def obtener_temperatura(self): # Metodo para obtener la temperatura
        return self._temperatura


class SemanaClima: # Clase para representar el clima de una semana
    def __init__(self):
        self.dias = []   # Lista de objetos ClimaDia

    def agregar_dia(self, temperatura): # Metodo para agregar un día con su temperatura
        self.dias.append(ClimaDia(temperatura))

    def promedio_semanal(self): # Metodo para calcular el promedio semanal
        if len(self.dias) == 0: # Evitar division por cero
            return 0
        total = sum(d.obtener_temperatura() for d in self.dias) # Suma de temperaturas
        return total / len(self.dias) # Retorna el promedio



# PROGRAMA PRINCIPAL

if __name__ == "__main__": # Punto de entrada del programa
    semana = SemanaClima() # Crear instancia de SemanaClima

    print("Ingresa las 7 temperaturas de la semana:") # Solicitar temperaturas al usuario
    for i in range(7): # Bucle para 7 días
        t = float(input(f"Temperatura día {i+1}: "))
        semana.agregar_dia(t)

    print(f"\nPromedio semanal: {semana.promedio_semanal():.2f} °C") # Mostrar el promedio semanal con dos decimales

