def ingresar_temperaturas(): # Función para ingresar temperaturas diarias
    temperaturas = [] # Lista para almacenar las temperaturas
    print("Ingrese las temperaturas diarias")
    for i in range (7): # Bucle para 7 días
        temp = float(input(f"Ingresa la temperatura del día {i+1}: "))
        temperaturas.append(temp)

    return temperaturas # Retorna la lista de temperaturas

def calcular_promedio(temps): # Función para calcular el promedio
    suma = sum(temps)
    promedio = suma / len(temps)
    return promedio

def main(): # Definimos la función principal
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)

    print("\nTemperaturas ingresadas:", temperaturas) # Muestra las temperaturas ingresadas
    print(f"Promedio semanal: {promedio:.2f} °C") # Muestra el promedio semanal con dos decimales


main() # Llamada a la función principal