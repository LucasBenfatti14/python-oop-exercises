from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    """
    Classe abstrata que tem como atributos, nome, sal_bruto, salario e como método abstrato calc_sal() e como método concreto analisar_sal()
    """

    nome: str
    sal_bruto: float
    salario: float

    SAL_MINIMO: int = 1612
    INSS: float = 7.5

    def __init__(self, nome: str = "None") -> None:
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calc_sal(self) -> None:
        pass

    def analisar_sal(self) -> None:
        analise = Panel(f"O salário de [blue]{self.nome}[/] ([magenta]{self.__class__.__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.salario / Funcionario.SAL_MINIMO:.1f} salários mínimos[/].", title="Análise de Salário", width=60)
        print(analise)


class Horista(Funcionario):
    """
    Sub classe de Funcionario que herda os atributos nome, sal_bruto, salario e tem os atributos valor_hora e horas_trab o método analisar_sal() com o método concreto herdado de Funcionario calc_sal()

    Para criar um novo horista, use:
    variavel = Horista(nome, valor_hora, horas_trab)
    """

    valor_hora: float
    horas_trab: float

    def __init__(self, nome: str, valor_hora: float, horas_trab: float) -> None:
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab

    def calc_sal(self) -> None:
        self.salario = self.sal_bruto * ((100 - Funcionario.INSS) / 100)


class Mensalista(Funcionario):
    """
    Sub classe de Funcionario que herda os atributos nome, sal_bruto, salario e o método analisar_sal() com o método concreto herdado de Funcionario calc_sal()

    Para criar um novo mensalista, use:
    variavel = Mensalista(nome, sal_bruto)
    """

    def __init__(self, nome: str, sal_bruto: float = Funcionario.SAL_MINIMO) -> None:
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self) -> None:
        self.salario = self.sal_bruto * ((100 - Funcionario.INSS) / 100)
