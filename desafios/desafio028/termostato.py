class Termostato:
    """
    Cria um termostato com o atributo privado temperatura que começa em 24 graus sendo possível mudar sua temperatura de 16 graus até 30 graus celsius, o valor da temperatura precisa ser divisível por 0.5

    Para criar um novo termostato, use:
    variavel = Termostato()
    """

    temperatura: float

    TEMPERATURA_MINIMA: int = 16
    TEMPERATURA_MAXIMA: int = 30

    def __init__(self) -> None:
        self.__temperatura = 24

    @property
    def temperatura(self) -> float:
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor: float) -> None:
        if valor < Termostato.TEMPERATURA_MINIMA:
            self.__temperatura = Termostato.TEMPERATURA_MINIMA
        elif valor > Termostato.TEMPERATURA_MAXIMA:
            self.__temperatura = Termostato.TEMPERATURA_MAXIMA
        elif valor % 0.5 == 0:
            self.__temperatura = valor
        else:
            raise ValueError(f"Temperatura de {valor}°C é inválida!")
        
    @property
    def ftemperatura(self) -> str:
        return (f"{self.__temperatura:.1f}°C")
