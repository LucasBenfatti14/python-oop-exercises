from retangulo import Retangulo
from rich import print, inspect


def main():
    r = Retangulo()

    # r.base = 12
    # r.altura = 4

    r.medidas = (8)

    print(r.medidas)
    inspect(r, private=True, methods=True)


if __name__ == "__main__":
    main()
