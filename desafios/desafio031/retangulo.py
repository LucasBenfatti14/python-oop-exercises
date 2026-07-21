class Retangulo:
    """
    Cria um retangulo com os atributos base e altura, que podem ser atribuídos, e área apenas calculado, setter medidas recebe uma tupla com os valores de base e altura respectivamente e o getter medidas mostra os dados formatados.

    Para criar um novo retangulo, use:
    variavel = Retangulo(base(opcional), altura(opcional))
    """

    base: float
    altura: float

    def __init__(self, base: float = 1, altura: float = 1) -> None:
        self._base = None
        self._altura = None

        self.base = base
        self.altura = altura

    @property
    def altura(self) -> float:
        return self._altura
    
    @altura.setter
    def altura(self, valor: float) -> None:
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("O valor da altura deve ser um número!")
        if valor < 0:
            raise ValueError("Valor inválido para altura!")
        self._altura = valor
    
    @property
    def area(self) -> float:
        return self._base * self._altura
    
    @area.setter
    def area(self, valor) -> float:
        raise PermissionError("Área não pode ser configurada desse jeito.")
    
    @property
    def base(self) -> float:
        return self._base
    
    @base.setter
    def base(self, valor: float) -> None:
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("O valor da base deve ser um número")
        if valor < 0:
            raise ValueError("Valor inválido para base!")
        self._base = valor

    @property
    def medidas(self) -> str:
        return f"Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}"
    
    @medidas.setter
    def medidas(self, valores: tuple) -> None:
        if not isinstance(valores, tuple):
            raise TypeError("As medidas devem ser informadas dentro de uma tupla")
        if len(valores) != 2:
            raise TypeError("Informe uma tupla com apenas dois valores numéricos")
        base, altura = valores
        self.base = base
        self.altura = altura
    