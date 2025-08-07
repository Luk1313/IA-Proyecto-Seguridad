import hashlib
import random
import string

class SistemaBancario:
    def __init__(self):
        self.cuentas = {}

    def es_contraseña_segura(self, contraseña):
        """
        Verifica si la contraseña es segura.
        """
        if not contraseña:
            raise ValueError("La contraseña no debe estar vacía.")

        tiene_mayuscula = any(c.isupper() for c in contraseña)
        tiene_minuscula = any(c.islower() for c in contraseña)
        tiene_numero = any(c.isdigit() for c in contraseña)
        return tiene_mayuscula and tiene_minuscula and tiene_numero

    def suma_recursiva(self):
        """
        Suma números ingresados por el usuario hasta que se ingresa un espacio en blanco.
        """
        entrada = input("Introduce un número (o espacio en blanco para terminar): ")
        if entrada.strip() == "":
            return 0
        try:
            numero = float(entrada)
        except ValueError:
            print("Error: ingresa un número válido.")
            return self.suma_recursiva()
        return numero + self.suma_recursiva()

    class Cuenta:
        def __init__(self, numero_cuenta, titular, saldo_inicial, tipo_cuenta):
            if saldo_inicial < 0:
                raise ValueError("El saldo inicial no puede ser negativo.")

            self.numero_cuenta = numero_cuenta
            self.titular = titular
            self.saldo = saldo_inicial
            self.tipo_cuenta = tipo_cuenta

        def depositar(self, cantidad):
            if cantidad <= 0:
                raise ValueError("La cantidad a depositar debe ser positiva.")
            self.saldo += cantidad
            print(f"Se han depositado {cantidad}. Nuevo saldo: {self.saldo}")

        def retirar(self, cantidad):
            if cantidad <= 0:
                raise ValueError("La cantidad a retirar debe ser positiva.")
            if cantidad > self.saldo:
                print(f"Saldo insuficiente para retirar {cantidad}. Saldo actual: {self.saldo}")
            else:
                self.saldo -= cantidad
                print(f"Se han retirado {cantidad}. Nuevo saldo: {self.saldo}")

        def obtener_balance(self):
            return self.saldo

        def __str__(self):
            return (f"Número de cuenta: {self.numero_cuenta}\n"
                    f"Titular: {self.titular}\n"
                    f"Saldo actual: {self.saldo}\n"
                    f"Tipo de cuenta: {self.tipo_cuenta}")

    def crear_cuenta(self):
        print("\n--- Crear Nueva Cuenta ---")
        numero_cuenta = input("Introduce el número de cuenta: ")
        titular = input("Introduce el nombre del titular: ")
        try:
            saldo_inicial = float(input("Introduce el saldo inicial: "))
        except ValueError:
            print("Saldo inválido. Debe ser un número.")
            return

        tipo_cuenta = input("Introduce el tipo de cuenta (Ahorros/Corriente): ")

        cuenta = self.Cuenta(numero_cuenta, titular, saldo_inicial, tipo_cuenta)
        self.cuentas[numero_cuenta] = cuenta
        print("Cuenta creada exitosamente.\n")

    def gestionar_cuenta(self):
        print("\n--- Gestión de Cuenta ---")
        numero_cuenta = input("Introduce el número de cuenta: ")
        cuenta = self.cuentas.get(numero_cuenta)

        if not cuenta:
            print("Número de cuenta no encontrado.")
            return

        while True:
            accion = input("¿Deseas depositar (d), retirar (r) o consultar saldo (s)? (o 'salir' para terminar): ").lower()
            if accion == 'd':
                try:
                    cantidad = float(input("Introduce la cantidad a depositar: "))
                    cuenta.depositar(cantidad)
                except ValueError:
                    print("Cantidad inválida.")
            elif accion == 'r':
                try:
                    cantidad = float(input("Introduce la cantidad a retirar: "))
                    cuenta.retirar(cantidad)
                except ValueError:
                    print("Cantidad inválida.")
            elif accion == 's':
                print(f"Saldo actual: {cuenta.obtener_balance()}")
            elif accion == 'salir':
                print("Sesión cerrada.\n")
                break
            else:
                print("Acción no válida.")

# --- Ejecución del programa ---
sistema = SistemaBancario()

# Verificación de contraseña segura
try:
    contraseña = input("Introduce una contraseña: ")
    if sistema.es_contraseña_segura(contraseña):
        print("La contraseña es segura.")
    else:
        print("La contraseña no es segura.")
except ValueError as e:
    print(f"Error: {e}")

# Suma recursiva de números
print("\n--- Suma Recursiva ---")
resultado = sistema.suma_recursiva()
print(f"La suma total es: {resultado}\n")

# Crear una nueva cuenta
sistema.crear_cuenta()

# Gestión de la cuenta
sistema.gestionar_cuenta()

