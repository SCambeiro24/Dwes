import random

def elegir_nivel():

    while True:
        nivel = input("Elige un nivel (fácil / medio / difícil): ").strip().lower()

        if nivel == "fácil" or nivel == "facil":
            return 50
        elif nivel == "medio":
            return 100
        elif nivel == "difícil" or nivel == "dificil":
            return 500
        else:
            print("Nivel no válido. Debe ser: fácil, medio o difícil.\n")


def pedir_numero(mensaje):

    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes introducir un número entero.\n")


def jugar():

    print("Bienvenido a 'Adivina el Número'")
    print("El programa pensará un número entre 1 y un máximo que tú elijas.")
    print("Tu objetivo es adivinarlo en el menor número de intentos.\n")

    maximo = elegir_nivel()
    numero_secreto = random.randint(1, maximo)

    intentos = 0

    print(f"\nHe pensado un número entre 1 y {maximo}. Intenta adivinarlo.\n")

    while True:
        intento = pedir_numero("Introduce tu número: ")
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo.\n")
        elif intento > numero_secreto:
            print("Demasiado alto.\n")
        else:
            print(f"Adivinaste el número en {intentos} intentos.\n")
            break


def main():

    while True:
        jugar()

        otra = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if otra != "s":
            print("\nGracias por jugar.")
            break


if __name__ == "__main__":
    main()
