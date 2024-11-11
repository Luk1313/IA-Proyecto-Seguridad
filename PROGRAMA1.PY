class SistemaBancario:
    def __init__(self):
        self.cuentas = {}

    def es_contraseña_segura(self, contraseña):
        """
        Verifica si la contraseña es segura.
        """
        assert len(contraseña) > 0, "La contraseña no debe estar vacía."
        tiene_mayuscula = any(c.isupper() for c in contraseña)
        tiene_minuscula = any(c.islower() for c in contraseña)
        tiene_numero = any(c.isdigit() for c in contraseña)
        return tiene_mayuscula and tiene_minuscula and tiene_numero

    def suma_recursiva(self):
        """
        Suma números ingresados por el usuario hasta que se ingresa un espacio en blanco.
        """
        entrada = input("Introduce un número (o espacio en blanco para terminar): ")
        if entrada == "":
            return 0
        try:
            numero = float(entrada)
        except ValueError:
            print("Error: ingresa un número válido.")
            return self.suma_recursiva()
        return numero + self.suma_recursiva()

    class Cuenta:
        def __init__(self, numero_cuenta, titular, saldo_inicial, tipo_cuenta):
            assert saldo_inicial >= 0, "El saldo inicial no puede ser negativo."
            self.numero_cuenta = numero_cuenta
            self.titular = titular
            self.saldo = saldo_inicial
            self.tipo_cuenta = tipo_cuenta

        def depositar(self, cantidad):
            assert cantidad > 0, "La cantidad a depositar debe ser positiva."
            self.saldo += cantidad
            print(f"Se han depositado {cantidad}. Nuevo saldo: {self.saldo}")

        def retirar(self, cantidad):
            assert cantidad > 0, "La cantidad a retirar debe ser positiva."
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Se han retirado {cantidad}. Nuevo saldo: {self.saldo}")
            else:
                print(f"Saldo insuficiente para retirar {cantidad}. Saldo actual: {self.saldo}")

        def obtener_balance(self):
            return self.saldo

        def __str__(self):
            return (f"Número de cuenta: {self.numero_cuenta}\n"
                    f"Titular: {self.titular}\n"
                    f"Saldo actual: {self.saldo}\n"
                    f"Tipo de cuenta: {self.tipo_cuenta}")

    def crear_cuenta(self, numero_cuenta, titular, saldo_inicial, tipo_cuenta):
        cuenta = self.Cuenta(numero_cuenta, titular, saldo_inicial, tipo_cuenta)
        self.cuentas[numero_cuenta] = cuenta
        print("Cuenta creada exitosamente.")

    def gestionar_cuenta(self):
        numero_cuenta = input("Introduce el número de cuenta: ")
        if numero_cuenta in self.cuentas:
            cuenta = self.cuentas[numero_cuenta]
            while True:
                accion = input("¿Deseas depositar (d), retirar (r) o consultar saldo (s)? (o 'salir' para terminar): ").lower()
                if accion == 'd':
                    cantidad = float(input("Introduce la cantidad a depositar: "))
                    cuenta.depositar(cantidad)
                elif accion == 'r':
                    cantidad = float(input("Introduce la cantidad a retirar: "))
                    cuenta.retirar(cantidad)
                elif accion == 's':
                    print(f"Saldo actual: {cuenta.obtener_balance()}")
                elif accion == 'salir':
                    break
                else:
                    print("Acción no válida.")
        else:
            print("Número de cuenta no encontrado.")

# Ejemplo de uso
sistema = SistemaBancario()

# Verificar contraseña
contraseña = input("Introduce una contraseña: ")
if sistema.es_contraseña_segura(contraseña):
    print("La contraseña es segura.")
else:
    print("La contraseña no es segura.")

# Sumar números
resultado = sistema.suma_recursiva()
print(f"La suma total es: {resultado}")

# Crear una cuenta
sistema.crear_cuenta(numero_cuenta="123456789", titular="Juan Pérez", saldo_inicial=1000, tipo_cuenta="Ahorros")

# Gestionar la cuenta
sistema.gestionar_cuenta()
