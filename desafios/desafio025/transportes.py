from abc import ABC, abstractmethod


class Transporte(ABC):
    """
    Classe abstrata que tem como atributos distância e frete e como método abstrado calc_frete()
    """

    distancia: float
    frete: float

    def __init__(self, distancia: float) -> None:
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self) -> str:
        pass


class Moto(Transporte):
    """
    Cria uma moto com um método concreto herdado de Transporte calc_frete().

    Para criar uma nova moto, use:
    variavel = Moto(distancia)
    """

    FATOR: float = 0.50

    def __init__(self, distancia: float) -> None:
        super().__init__(distancia)
    
    def calc_frete(self) -> str:
        self.frete = self.distancia * Moto.FATOR 
        return f"R${self.frete:.2f}"
    

class Drone(Transporte):
    """
    Cria um drone com um método concreto herdado de Transporte calc_frete().

    Para criar um novo drone, use:
    variavel = Drone(distancia)
    """

    FATOR: float = 9.50

    def __init__(self, distancia: float) -> None:
        super().__init__(distancia)

    def calc_frete(self) -> str:
        if self.distancia > 10:
            return "Raio máximo de 10km"
        self.frete = self.distancia * Drone.FATOR
        return f"R${self.frete:.2f}"


class Caminhao(Transporte):
    """
    Cria um caminhão com um método concreto herdado de Transporte calc_frete().

    Para criar um novo caminhão, use:
    variavel = Caminhao(distancia)
    """

    FATOR:float = 1.20

    def __init__(self, distancia: float) -> None:
        super().__init__(distancia)

    def calc_frete(self) -> str:
        if self.distancia < 50:
            return "Raio mínimo de 50km"
        self.frete = self.distancia * Caminhao.FATOR
        return f"R${self.frete:.2f}"
