from diario import Diario
from rich import print, inspect


def main():
    d = Diario()
    d.senha = "1234"
    print(d.senha)

    d.escrever("Primeira mensagem")
    d.escrever("Você é uma pessoa simpática")
    d.escrever("Você gosta de Python")

    d.ler("1235")

    inspect(d, private=True, methods=True)


if __name__ == "__main__":
    main()
