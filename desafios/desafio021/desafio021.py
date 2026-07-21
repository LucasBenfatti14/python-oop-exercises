from rich import print

class Caneta:
    """
    Cria uma caneta da cor desejada, usando o método destampar() é possível prepará-la para escrever, ao usar o método escrever() é exibido a mensagem na tela com a cor da centa, e o método quebrar_linha()

    Para criar uma nova caneta, use
    variavel = Caneta(cor)
    """
    
    cor: str
    tampa: bool


    def __init__(self, cor: str = "azul") -> None:
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampa = True

    def destampar(self) -> None:
        self.tampa = False

    def tampar(self) -> None:
        self.tampa = True

    def escrever(self, texto: str) -> None:
        if self.tampa:
            print(f":prohibited: A {self.cor}Caneta[/] está tampada!")
        else:
            print(f"{self.cor}{texto}[/]", end=" ")

    def quebrar_linha(self, qtd_linhas: int = 1):
        print("\n" * qtd_linhas)


# Programa Principal
c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto!")
c3.escrever("Vamos exercitar!")
