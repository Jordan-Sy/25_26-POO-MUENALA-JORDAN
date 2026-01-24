class CuentaBancaria:  # Definición de la clase. Clase que representa una cuenta bancaria simple.

    def __init__(self, titular, saldo_inicial): # Constructor: se ejecuta al crear el objeto.

        self.titular = titular
        self.saldo = saldo_inicial
        print(f"[INFO] Cuenta creada para {self.titular} con saldo ${self.saldo}")

    def depositar(self, monto): # Método para depositar dinero en la cuenta.

        self.saldo += monto
        print(f"[INFO] Depósito de ${monto} realizado. Saldo actual: ${self.saldo}")

    def retirar(self, monto): # Método para retirar dinero de la cuenta.

        if monto <= self.saldo:
            self.saldo -= monto
            print(f"[INFO] Retiro de ${monto} realizado. Saldo actual: ${self.saldo}")
        else:
            print("[ERROR] Saldo insuficiente.")

    def mostrar_saldo(self): # Muestra el saldo actual de la cuenta.

        print(f"[INFO] Saldo de {self.titular}: ${self.saldo}")

    def __del__(self): #  Destructor: se ejecuta cuando el objeto se elimina.

        print(f"[INFO] Cuenta de {self.titular} cerrada y eliminada de la memoria.")


# -------------------------------
# PROGRAMA PRINCIPAL


if __name__ == "__main__": # Punto de entrada del programa.
    print("=== Bienvenido al Banco ===\n")

    # Crear una cuenta bancaria (se llama al constructor)
    cuenta1 = CuentaBancaria("Jordan", 600)

    # Usar métodos de la cuenta
    cuenta1.mostrar_saldo()
    cuenta1.depositar(200)
    cuenta1.retirar(100)
    cuenta1.mostrar_saldo()

    print("\n----------------------------\n")

    # Eliminar la cuenta manualmente para activar el destructor
    del cuenta1

    print("\n Fin del programa bancario.")

