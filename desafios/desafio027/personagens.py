from abc import ABC, abstractmethod
from rich import print
from random import randint, randrange


class Personagem(ABC):
    """
    Classe abstrata que tem como atributos nome e vida com o método atacar(alvo, forca), e com o método abstrato curar()
    """

    nome: str
    vida: int

    def __init__(self, nome: str, vida: int) -> None:
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo: "Personagem", forca: int = 100) -> None:
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[randrange(0, len(self.golpes))]
            print(f"[green]{self.nome}[/]([cyan]{self.vida}[/]) atacou [red]{alvo.nome}[/]([cyan]{alvo.vida}[/]) com um [blue]{golpe}[/] de força [cyan]{forca}[/]")
            alvo.receber_dano(forca)
        else:
            print(f"O Ataque {self.nome} -> {alvo.nome} não pode acontecer")

    def receber_dano(self, dano: int) -> None:
        ataque = randint(0, dano)
        self.vida -= ataque
        if self.vida < 0:
            self.vida = 0
        print(f"[blue]{self.nome}[/] recebeu [red]dano de {ataque}[/]!")

    @abstractmethod
    def curar(self) -> None:
        pass


class Guerreiro(Personagem):
    """
    Sub classe de Personagens com os atributos herdados nome e vida e com o método concreto herdado curar().

    Para criar um novo guerreiro, use:
    variavel = Guerreiro(nome, vida)
    """ 

    def __init__(self, nome: str, vida: int) -> None:
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Pulo giratório", "Golpe de Machado"]

    def curar(self) -> None:
        pontos_recuperados = randint(0, 100)
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou[/] {pontos_recuperados} pontos de vida.")
        self.vida += pontos_recuperados


class Mago(Personagem):
    """
    Sub classe de Personagens com os atributos herdados nome e vida e com o método concreto herdado curar().

    Para criar um novo mago, use:
    variavel = Mago(nome, vida)
    """

    def __init__(self, nome: str, vida: int) -> None:
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio de Luz", "Magia Estática"]

    def curar(self) -> None:
        pontos_recuperados = randint(0, 100)
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou[/] {pontos_recuperados} pontos de vida.")
        self.vida += pontos_recuperados
