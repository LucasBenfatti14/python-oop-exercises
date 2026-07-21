from hashlib import sha256


class ContaBancaria:
    """
    Cria uma conta bancária com id, titular, saldo e senha, caso a senha não seja colocana na instanciação ela será pedida ao usuário.
    Além desse possui os métodos públicos: sacar(valor, chave(opcional)), depositar(valor).
    A senha é criptografa usando sha256 da biblioteca hashlib.

    Para criar uma nova conta bancária, use:
    variavel = ContaBancaria(id, nome, saldo, senha(opcional))
    """

    _id: int
    _titular: str
    __saldo: float
    __hash: str

    def __init__(self, id: int, nome: str, saldo: float, senha: str|None = None) -> None:
        self._id = id
        if len(nome.strip()) <= 3:
            raise ValueError("O nome precisa ter mais que 3 caracteres")
        self._titular = nome
        if saldo < 0:
            raise ValueError("A conta não pode começar com um valor negativo!")
        self.__saldo = saldo

        if not senha:
            senha = self.pede_senha()
        senha_codificada = self.codificar(senha)
        self.__hash = senha_codificada
        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def nome(self) -> str:
        return self._titular
    
    @nome.setter
    def nome(self, nome_novo: str) -> None:
        senha = self.pede_senha()
        if self.validar_senha(senha):
            if len(nome_novo.strip()) > 3:
                self._titular = nome_novo
                print(f"O nome de usuário foi alterado para {nome_novo} com sucesso!")
            else:
                print("O nome de usuário precisa ter mais que 3 caracteres")
        else:
            print("Senha incorreta. Impossível mudar seu nome!")

    def validar_senha(self, chave: str) -> bool:
        hash_digitado = self.codificar(chave)
        return hash_digitado == self.__hash

    def pede_senha(self) -> str:
        senha = input("Senha: ")
        if len(senha.strip()) < 4:
            raise ValueError("A senha precisa ter pelo menos 4 dígitos!")
        return senha
    
    def codificar(self, senha: str) -> str:
        return sha256(senha.encode("utf-8")).hexdigest()

    def sacar(self, valor: float, chave: str = None) -> None:
        if valor <= 0:
            raise ValueError("O valor do saque precisa ser positivo!")
        if valor > self.__saldo:
            raise ValueError("Você não tem essa quantia como saldo na sua conta!")
        if not chave:
            chave = self.pede_senha()
        if self.validar_senha(chave):
            self.__saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self._id}")
        else:
            print("SENHA ERRADA! SAQUE NÃO AUTORIZADO.")

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito precisa ser positivo!")
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self._id}")
