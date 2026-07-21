from credencial import Credencial
from rich import print, inspect


def main():
    c = Credencial()
    c.senha = input("Digite a sua senha: ")
    print(c.senha)

    if c.validar("Guanabara"):
        print("Acertei a senha!")
    else:
        print("Errei a senha!")

if __name__ == "__main__":
    main()