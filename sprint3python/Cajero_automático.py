def pedir_cantidad(mensaje):
    while True:
        try:
            cantidad = float(input(mensaje))
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser positiva.\n")
        except ValueError:
            print("Debes introducir un número válido.\n")


def mostrar_menu():
    print("MENÚ DEL CAJERO")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    print("---------------------------")


def consultar_saldo(cuenta):
    print(f"Saldo actual: {cuenta['saldo']:.2f} €\n")


def ingresar_dinero(cuenta):
    cantidad = pedir_cantidad("Cantidad a ingresar: ")
    cuenta["saldo"] += cantidad
    print(f"Has ingresado {cantidad:.2f} €. Nuevo saldo: {cuenta['saldo']:.2f} €\n")


def retirar_dinero(cuenta):
    while True:
        try:
            cantidad = float(input("Cantidad a retirar: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.\n")
            elif cantidad > cuenta["saldo"]:
                print("Saldo insuficiente.\n")
            else:
                cuenta["saldo"] -= cantidad
                print(f"Has retirado {cantidad:.2f} €. Nuevo saldo: {cuenta['saldo']:.2f} €\n")
                return
        except ValueError:
            print("Debes introducir un número válido.\n")

def main():

    cuenta = {"nombre": "Ana", "saldo": 1200.0}

    print(f"Bienvenida/o, {cuenta['nombre']}.\n")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            consultar_saldo(cuenta)
        elif opcion == "2":
            ingresar_dinero(cuenta)
        elif opcion == "3":
            retirar_dinero(cuenta)
        elif opcion == "4":
            print("Gracias por usar el cajero. Hasta pronto.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.\n")


if __name__ == "__main__":
    main()