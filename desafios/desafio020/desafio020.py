from rich import print
from rich.panel import Panel

class Gamer:
    """
    Cria um gamer com nome e nick e através do método add_favoritos() é possível adicionar jogos à lista de favoritos do mesmo, e através do método ficha() são mostrados o nome, nick e lista de favoritos em ordem alfabética

    Para criar um novo gamer, use
    variavel = Gamer(nome, nick)
    """

    nome: str
    nick: str
    favoritos: list

    def __init__(self, nome: str, nick: str) -> None:
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self, jogo: str) -> None:
        self.favoritos.append(jogo)

    def ficha(self) -> None:
        self.favoritos.sort()
        conteudo = f"Nome Real: [white on blue] {self.nome} [/]\n"
        conteudo += f"Jogos Favoritos:"
        for jogo in self.favoritos:
            conteudo += f"\n:video_game: [blue]{jogo}[/]"
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print(painel)
    

# Programa Principal
j1 = Gamer("Fabricio da Silva", "detonator2026")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God od War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer("Olívia Souza", "peach_raivosa")
j2.add_favoritos("Mario Bros")
j2.add_favoritos("Call Of Duty")
j2.ficha()