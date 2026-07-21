from rich import print
from time import sleep

class Livro:
    """
    Cria um livro com título e número de páginas, e através de um método é possível avançar páginas nesse livro, ao chegar no final do livro, exibe uma mensagem ao usuário

    Para criar um novo livro, use
    variavel = Livro(titulo, paginas)
    """

    titulo: str
    paginas: int
    pagina_atual: int

    def __init__(self, titulo: str, paginas: int) -> None:
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f":open_book:[blue] Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total. Você agora está na [yellow]página {self.pagina_atual}[/]")

    def avancar_paginas(self, qtd_paginas: int = 1) -> None:
        if qtd_paginas < 0:
            print(f"[red]Não é possível avançar {qtd_paginas} páginas[/]")
        cont_paginas_passadas = 0
        for i in range(0, qtd_paginas):
            if self.pagina_atual >= self.paginas:
                break
            cont_paginas_passadas += 1 
            self.pagina_atual += 1
            print(f"Pág{self.pagina_atual} :arrow_forward: ", end="")
            sleep(0.3)
        print(f"[blue]Você avançou {cont_paginas_passadas} páginas e agora está na[/] [yellow]página {self.pagina_atual}[/]")
        if self.pagina_atual == self.paginas:
            print(f"[red]:closed_book: Você chegou ao final do livro '{self.titulo}'[/]")


# Programa Principal
l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(4)
l1.avancar_paginas(11)
l1.avancar_paginas(500)
