from rich import print
from hashlib import sha256


class Diario:
    """
    Cria um diário com uma senha, qualquer pessoa pode usar o método escrever(msg) para escrever mensagens nesse diário, mas somente quem souber a senha passada por parâmetro na classe que poderá usar o método ler(senha).

    Para criar um novo diário, use:
    variavel = Diario(senha)
    """

    __senha: str
    __segredos: list[str]

    def __init__(self) -> None:
        self.__segredos = []
        self.__senha = None

    def codificar_senha(self, senha: str) -> str:
        return sha256(senha.encode("utf-8")).hexdigest()

    def pedir_senha(self) -> str:
        senha = input("Para trocar sua senha digite sua senha atual: ")
        return senha
    
    def validar_senha_atual(self) -> None:
        senha_atual = self.pedir_senha()
        hash_atual = self.codificar_senha(senha_atual)
        if hash_atual != self.__senha:
            raise PermissionError("Senha atual inválida!")
    
    def validar_nova_senha(self, nova_senha: str) -> None:
        if len(nova_senha) < 4:
            raise ValueError("Sua nova senha precisa ter pelo menos 4 caracteres!")

    @property
    def senha(self) -> None:
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha: str) -> None:
        if self.__senha != None:
            self.validar_senha_atual()
        self.validar_nova_senha(nova_senha)
        hash_atual = self.codificar_senha(nova_senha)
        self.__senha = hash_atual

    def escrever(self, msg: str) -> None:
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())
        else:
            raise ValueError("Essa mensagem não é válida!")

    def ler(self, senha: str) -> None:
        hash_atual = self.codificar_senha(senha)
        if hash_atual != self.__senha:
            raise PermissionError("Senha inválida! Você não pode ler meu diário!")
        print("[green]Diário LIBERADO![/]")
        for msg in self.__segredos:
            print(f"- {msg}")
        print()
