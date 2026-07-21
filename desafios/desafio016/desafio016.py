from rich import print

class Funcionario:
    """
    Cria um funcionário com nome, setor e cargo e permite usar o método apresentar()
    para que seja explicitado seu estado.
    """
    # Atributos de Classe
    EMPRESA = "Curso em Vídeo"

    nome: str
    setor: str
    cargo: str

    def __init__(self, nome:str, setor:str, cargo:str) -> None:
        # Atributos de Instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> str:
        return f":vulcan_salute: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.EMPRESA}"


# Programa Principal
c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentar())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentar())
