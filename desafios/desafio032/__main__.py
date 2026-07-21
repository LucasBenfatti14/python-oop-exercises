from conta_bancaria import ContaBancaria
from rich import print, inspect


def main():
    print("Criando a conta")
    cc = ContaBancaria(123, "Gustavo", 1000)

    print("Realizando depósito")
    cc.depositar(500)

    print("Realizando saque")
    cc.sacar(200)

    cc.nome = "Manoel"

    inspect(cc, private=True, methods=True)


if __name__ == "__main__":
    main()
