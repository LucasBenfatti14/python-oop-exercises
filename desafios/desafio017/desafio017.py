from rich import print
from rich.panel import Panel

class Produto:
    """
    Cria um produto com nome e preço, e o método etiqueta() permite explicitar seu estado na forma de uma etiqueta
    """

    nome: str
    preco: float

    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def etiqueta(self) -> None:
        etq = Panel(f"{self.nome:^30}\n{"-"*31}{self.preco:.^31,.2f}", title="Produto", width=35)
        print(etq)


# Programa Principal
p1 = Produto("Iphone 17 Pro Max", 25000.85)
p2 = Produto("Notebook Gamer", 8000)
p3 = Produto("Mouse", 120)

p1.etiqueta()
p2.etiqueta()
p3.etiqueta()
