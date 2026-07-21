from abc import ABC
from datetime import date


class Pessoa(ABC):
    """
    Classe abstrata com os atributos protegidos _nome e _nascimento, com getter e setter de nascimento, e getter de idade.
    """

    ANO_ATUAL: int = date.today().year

    _nome: str
    _nascimento: int

    def __init__(self, nome: str, nascimento: int) -> None:
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento

    @property
    def nascimento(self) -> int:
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano: int) -> None:
        if ano > Pessoa.ANO_ATUAL or ano < (Pessoa.ANO_ATUAL - 150):
            raise ValueError(f"Ano {ano} é inválido")
        self._nascimento = ano

    @property
    def idade(self) -> int:
        return Pessoa.ANO_ATUAL - self._nascimento
    
    @idade.setter
    def idade(self, valor: int) -> None:
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento")


class Aluno(Pessoa):
    """
    Sub Classe de Pessoa, herda os atributos nome e nascimento, e tem os atributos próprios _curso e cursos_oficiais, possui getter e setter de curso e o método público add_curso que permite adicionar um curso à lista de cursos oficiais.

    Para criar um novo aluno, use:
    variavel = Aluno(nome, nascimento, curso)
    """
    _curso: str
    cursos_oficiais: list[str]

    def __init__(self, nome: str, nascimento: int, curso: str) -> None:
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]
        self._curso = None
        self.curso = curso

    @property
    def curso(self) -> str:
        return self._curso

    @curso.setter
    def curso(self, curso: str) -> None:
        if curso not in self.cursos_oficiais:
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais.")
        self._curso = curso

    def add_curso(self, curso: str) -> None:
        curso = curso.strip()
        if len(curso) >= 3:
            if curso not in self.cursos_oficiais:
                self.cursos_oficiais.append(curso)
            else:
                raise ValueError(f"O curso {curso} já está na lista.")
        else:
            raise ValueError(f"O nome do curso precisa ter pelo menos 3 caracteres!")
