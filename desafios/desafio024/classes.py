from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    """
    Classe abstrata que tem como métodos concretos preparar() e ferver_agua() e como métodos abstratos misturar() e servir()
    """

    def preparar(self) -> None:
        print(f"--- Iniciando o Preparo ---")
        print(f"1. {self.ferver_agua()}")
        print(f"2. {self.misturar()}")
        print(f"3. {self.servir()}")
        print(f"--- Bebida Pronta ---\n")


    def ferver_agua(self) -> str:
        return "Fervendo a água a 100 graus Celsius"

    @abstractmethod
    def misturar(self) -> str:
        pass

    @abstractmethod
    def servir(self) -> str:
        pass


class Cafe(BebidaQuente):
    """
    Cria um café com dois métodos abstratos herdados de BebidaQuente: misturar() e servir().
    
    Para criar um novo café, use:
    variavel = Cafe()
    """

    def misturar(self) -> str:
        return "Passando água pressurizada pelo pó de café moído."

    def servir(self) -> str:
        return "Servindo em xícara pequena."


class Cha(BebidaQuente):
    """
    Cria um chá com dois métodos abstratos herdados de BebidaQuente: misturar() e servir().

    Para criar um novo chá, use:
    variavel = Cha()
    """

    def misturar(self) -> str:
        return "Mergulhando o sachê de ervas na água."

    def servir(self) -> str:
        return "Servindo na caneca de porcelana com limão."


class Leite(BebidaQuente):
    """
    Cria um leite com dois métodos abstratos herdados de BebidaQuente: misturar() e servir().

    Para criar um novo leite, use:
    variavel = Leite()
    """

    def misturar(self) -> str:
        return "Passando vapor pressurizado pelo bico do leite."

    def servir(self) -> str:
        return "Servindo na caneca grande, já com café."
