import random
import unicodedata

PALABRAS = [
    "programacion", "ordenador", "teclado", "pantalla", "memoria",
    "algoritmo", "variable", "funcion", "bucle", "compilador",
    "internet", "servidor", "navegador", "contrasena", "archivo",
    "carpeta", "sistema", "proceso", "usuario", "consola",
    "sevilla", "guitarra", "naranja", "ventana", "montana",
]

MUNECO = [
    '     +---+\n         |\n         |\n         |\n        ===',
    '     +---+\n     O   |\n         |\n         |\n        ===',
    '     +---+\n     O   |\n     |   |\n         |\n        ===',
    '     +---+\n     O   |\n    /|   |\n         |\n        ===',
    '     +---+\n     O   |\n    /|\\  |\n         |\n        ===',
    '     +---+\n     O   |\n    /|\\  |\n    /    |\n        ===',
    '     +---+\n     O   |\n    /|\\  |\n    / \\  |\n        ===',
]

INTENTOS = len(MUNECO) - 1


def normalizar(texto):
    """Quita tildes, asi 'montaña' se puede escribir como 'montana'."""
    sin_tildes = unicodedata.normalize("NFD", texto)
    return "".join(c for c in sin_tildes if unicodedata.category(c) != "Mn").lower()


def mostrar_palabra(palabra, acertadas):
    return " ".join(letra if letra in acertadas else "_" for letra in palabra)


def pedir_letra(usadas):
    while True:
        entrada = input("\n  Letra: ").strip().lower()

        if len(entrada) != 1:
            print("  Una letra sola.")
            continue

        letra = normalizar(entrada)

        if not letra.isalpha():
            print("  Eso no es una letra.")
            continue

        if letra in usadas:
            print("  Esa ya la has dicho.")
            continue

        return letra


def jugar():
    palabra = normalizar(random.choice(PALABRAS))
    acertadas = set()
    falladas = set()

    print("\n  EL AHORCADO")
    print(f"  Palabra de {len(palabra)} letras.")

    while True:
        fallos = len(falladas)
        print("\n" + MUNECO[fallos])
        print(f"\n  {mostrar_palabra(palabra, acertadas)}")

        if falladas:
            print(f"\n  Falladas: {' '.join(sorted(falladas))}")

        print(f"  Te quedan {INTENTOS - fallos} intentos.")

        letra = pedir_letra(acertadas | falladas)

        if letra in palabra:
            acertadas.add(letra)

            # comprobamos si ya estan todas
            if all(l in acertadas for l in palabra):
                print("\n" + MUNECO[fallos])
                print(f"\n  {mostrar_palabra(palabra, acertadas)}")
                print(f"\n  Ganaste. Era '{palabra}'.")
                return True
        else:
            falladas.add(letra)

            if len(falladas) > INTENTOS:
                print("\n" + MUNECO[-1])
                print(f"\n  Te quedaste sin intentos. Era '{palabra}'.")
                return False


def main():
    ganadas = 0
    jugadas = 0

    while True:
        if jugar():
            ganadas += 1
        jugadas += 1

        print(f"\n  Llevas {ganadas} de {jugadas}.")

        if input("\n  Otra? (s/n) ").strip().lower() != "s":
            print()
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
