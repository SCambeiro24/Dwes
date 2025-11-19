import random


OPCIONES = ["piedra", "papel", "tijera", "lagarto", "spock"]


REGLAS = {
    "tijera": ["papel", "lagarto"],
    "papel": ["piedra", "spock"],
    "piedra": ["tijera", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["piedra", "tijera"]
}

def pedir_jugada():

    while True:
        jugada = input("Elige tu jugada (piedra, papel, tijera, lagarto, spock): ").strip().lower()
        if jugada in OPCIONES:
            return jugada
        print("Entrada no válida. Intenta de nuevo.\n")

def pedir_numero_rondas():

    while True:
        try:
            n = int(input("Número de rondas (debe ser impar y >= 1): "))
            if n >= 1 and n % 2 == 1:
                return n
            print("Debe ser un número impar mayor o igual que 1.\n")
        except ValueError:
            print("Debes introducir un número entero.\n")

def determinar_resultado(jugada_usuario, jugada_cpu):

    if jugada_usuario == jugada_cpu:
        return 0
    elif jugada_cpu in REGLAS[jugada_usuario]:
        return 1
    else:
        return -1


def jugar_ronda():

    jugada_usuario = pedir_jugada()
    jugada_cpu = random.choice(OPCIONES)

    print(f"Usuario: {jugada_usuario}")
    print(f"CPU: {jugada_cpu}")

    resultado = determinar_resultado(jugada_usuario, jugada_cpu)

    if resultado == 0:
        print("Resultado: Empate.\n")
    elif resultado == 1:
        print("Resultado: Gana el usuario.\n")
    else:
        print("Resultado: Gana la CPU.\n")

    return resultado

def jugar_partida():

    n = pedir_numero_rondas()
    victorias_necesarias = n // 2 + 1

    puntos_usuario = 0
    puntos_cpu = 0

    print(f"Comienza la partida al mejor de {n} rondas.\n")

    while puntos_usuario < victorias_necesarias and puntos_cpu < victorias_necesarias:
        resultado = jugar_ronda()

        if resultado == 1:
            puntos_usuario += 1
        elif resultado == -1:
            puntos_cpu += 1

        print(f"Marcador -> Usuario: {puntos_usuario} | CPU: {puntos_cpu}\n")

    if puntos_usuario > puntos_cpu:
        print("Ganador final: Usuario.\n")
    else:
        print("Ganador final: CPU.\n")

def main():

    while True:
        jugar_partida()

        repetir = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if repetir != "s":
            print("Gracias por jugar.")
            break

if __name__ == "__main__":
    main()
