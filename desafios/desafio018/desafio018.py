from rich.panel import Panel
from rich import print

class Churrasco:
    """
    Cria um evento de churrasco que recebe título e a quantidade de pessoas, calcula o total de carne que deve ser comprado, o custo total e o custo por pessoa

    Para criar um novo evento, use
    variavel = Churrasco(titulo, qnt_pessoas)
    """

    titulo: str
    qnt_pessoas: int

    PRECO_KG: float = 82.4
    CONSUMO_PESSOA: float = 0.4

    def __init__(self, titulo: str, qnt_pessoas: int) -> None:
        self.titulo = titulo
        self.qnt_pessoas = qnt_pessoas

    def calcular_quantidade_carne(self) -> float:
        return self.qnt_pessoas * Churrasco.CONSUMO_PESSOA
    
    def calcular_valor_total(self) -> float:
        return self.calcular_quantidade_carne() * Churrasco.PRECO_KG
    
    def calcular_valor_individual(self) -> float:
        return self.calcular_valor_total() / self.qnt_pessoas
    
    def analisar(self) -> None:
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.qnt_pessoas} convidados[/]\n"
        conteudo += f"Cada participante comerá {Churrasco.CONSUMO_PESSOA:.1f}Kg e cada Kg custa R${Churrasco.PRECO_KG:,.2f}\n"
        conteudo += f"Recomendo [blue]comprar {self.calcular_quantidade_carne():.3f}Kg[/] de carne\n"
        conteudo += f"O custo total será de [green]R${self.calcular_valor_total():,.2f}[/]\n"
        conteudo += f"Cada pessoa pagará [yellow]R${self.calcular_valor_individual():,.2f}[/] para participar."
        analise = Panel(conteudo, title=self.titulo, width=100)
        print(analise)


# Programa Principal
c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()

c2 = Churrasco("Festa do fim de ano", 80)
c2.analisar()
