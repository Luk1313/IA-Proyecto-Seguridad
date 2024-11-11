
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
