import random


def jugar_juego():
    nombre = input("Ingresa tu nombre: ")
    print(f"Bueno {nombre}, he pensado un número entre 1 y 100.")

    numero_secreto = random.randint(1, 100)
    intentos = 8

    for intento in range(1, intentos + 1):
        guess = int(input("Intento {}/{} - Ingresa tu adivinanza: ".format(intento, intentos)))

        if guess == numero_secreto:
            print("¡Adivinaste!")
            return

        if guess < numero_secreto:
            print("El número es más grande.")
        else:
            print("El número es más pequeño.")

    print("Game over. El número era:", numero_secreto)


jugar_juego()