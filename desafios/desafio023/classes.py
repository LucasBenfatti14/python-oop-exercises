from abc import ABC, abstractmethod


class Poligono(ABC):
    """
    Essa classe é abstrata e tem como atributo a quantidade de lados de um polígono, além de dois métodos abstratos: perimetro() e area(). 
    """

    qtd_lados: int

    def __init__(self, qtd_lados: int) -> None:
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Quadrado(Poligono):
    """
    Cria um quadrado com o atributo qtd_lados herdado da classe Poligono, além de dois métodos abstratos herdados de Poligono, perimetro() e area(). Possui o atributo próprio: lado.

    Para criar um novo quadrado use:
    variavel = Quadrado(lado)
    """

    lado: float

    def __init__(self, lado: float) -> None:
        super().__init__(4)
        self.lado = lado

    def perimetro(self) -> float:
        return self.qtd_lados * self.lado

    def area(self) -> float:
        return self.lado ** 2


class Circulo(Poligono):
    """
    Cria um círculo com o atributo qtd_lados herdado da classe Poligono, além de dois métodos abstratos herdados de Poligono, perimetro() e area(). Possui o atributo próprio: raio.

    Para criar um novo circulo use:
    variavel = Circulo(raio)
    """

    raio: float
    PI: float = 3.1415

    def __init__(self, raio: float) -> None:
        super().__init__(0)
        self.raio = raio

    def perimetro(self) -> float:
        return 2 * Circulo.PI * self.raio
        
    def area(self) -> float:
        return Circulo.PI * self.raio ** 2
