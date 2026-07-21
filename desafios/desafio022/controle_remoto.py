from rich import print
from rich.panel import Panel
from funcoes import formatar_mensagem_importante

class ControleRemoto:
    """
    Cria um controle remoto para controlar uma televisão pelo terminal, é possível ligar e desligar a tv,
    avançar e retroceder nos canais e aumentar e diminuir o volume.

    Para criar um novo controle remoto, use:
    variavel = ControleRemoto()
    """

    tv_ligada: bool
    volume: int
    canal: int
    LARGURA_TELA_TV: int = 56
    LARGURA_TV: int = 60
    ALTURA_TV: int = 11
    VOLUME_MAXIMO: int = 5
    VOLUME_MINIMO: int = 0
    CANAL_MAXIMO: int = 5
    CANAL_MINIMO: int = 1

    def __init__(self) -> None:
        self.canal = 1
        self.volume = 2
        self.tv_ligada = False

    def comando_controle(self) -> str:
        try:
            comando = input(F"< CH{self.canal} >   - VOL{self.volume} +   ON/OFF @   SAIR DA SALA DE ESTAR 0   ")
            return comando
        except KeyboardInterrupt:
            formatar_mensagem_importante("red", "o usuário optou por não dar nenhum comando!", 0)
            return "0"

    def ligar_desligar_tv(self) -> None:
        if self.tv_ligada:
            self.tv_ligada = False
        else:
            self.tv_ligada = True

    def cor_tela_tv(self) -> str:
        match self.canal:
            case 1:
                return "[blue]"
            case 2:
                return "[green]"
            case 3:
                return "[yellow]"
            case 4:
                return "[red]"
            case 5:
                return "[white]"

    def mostrar_tv(self) -> Panel:
        tela = self.cor_tela_tv()
        if self.tv_ligada:
            estado_atual = f"{"-"*ControleRemoto.LARGURA_TELA_TV}{tela}{"*" * ControleRemoto.LARGURA_TELA_TV * 5}[/]{"-"*ControleRemoto.LARGURA_TELA_TV}CANAL  = [yellow]{self.canal}[/]\nVOLUME = {(":blue_square:" * self.volume) if self.volume > 0 else (":muted_speaker:")}"
        else:
            estado_atual = f"{"\n"*4}{" "*15}[red]:prohibited: A TV está desligada[/]"
        tv = Panel(f"{estado_atual}", title="TV", width=ControleRemoto.LARGURA_TV, height=ControleRemoto.ALTURA_TV)
        return tv

    def aumentar_volume(self) -> None:
        if self.volume < ControleRemoto.VOLUME_MAXIMO:
            self.volume += 1

    def diminuir_volume(self) -> None:
        if self.volume > ControleRemoto.VOLUME_MINIMO:
                    self.volume -= 1

    def avancar_canal(self) -> None:
        if self.canal == ControleRemoto.CANAL_MAXIMO:
            self.canal = ControleRemoto.CANAL_MINIMO
        else:
            self.canal += 1

    def voltar_canal(self) -> None:
        if self.canal == ControleRemoto.CANAL_MINIMO:
            self.canal = ControleRemoto.CANAL_MAXIMO
        else:
            self.canal -= 1
