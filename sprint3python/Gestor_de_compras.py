def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Ver lista")
    print("4. Vaciar lista")
    print("5. Salir")


def anadir_producto(lista):
    producto = input("Ingresa el nombre del producto: ").strip().lower()
    if producto == "":
        print("No puedes añadir un nombre vacío.")
        return
    if producto in lista:
        print(f"'{producto}' ya está en la lista.")
    else:
        lista.append(producto)
        print(f"'{producto}' añadido correctamente.")


def eliminar_producto(lista):
    if not lista:
        print(" La lista está vacía, no hay nada que eliminar.")
        return
    producto = input("Ingresa el producto que deseas eliminar: ").strip().lower()
    if producto in lista:
        lista.remove(producto)
        print(f"'{producto}' eliminado correctamente.")
    else:
        print(f"'{producto}' no se encuentra en la lista.")


def ver_lista(lista):
    if not lista:
        print(" Tu lista de la compra está vacía.")
    else:
        print("\nTu lista de la compra (ordenada alfabéticamente):")
        for i, producto in enumerate(sorted(lista), 1):
            print(f"{i}. {producto}")


def vaciar_lista(lista):
    if not lista:
        print(" La lista ya está vacía.")
        return
    confirmacion = input("¿Seguro que quieres vaciar la lista? (s/n): ").lower()
    if confirmacion == "s":
        lista.clear()
        print("Lista vaciada correctamente.")
    else:
        print("Operación cancelada.")


def main():
    lista_compra = []

    print("Bienvenido/a al Gestor de Lista de la Compra ")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            anadir_producto(lista_compra)
        elif opcion == "2":
            eliminar_producto(lista_compra)
        elif opcion == "3":
            ver_lista(lista_compra)
        elif opcion == "4":
            vaciar_lista(lista_compra)
        elif opcion == "5":
            print("¡Gracias por usar el gestor de la compra! Hasta la próxima.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()