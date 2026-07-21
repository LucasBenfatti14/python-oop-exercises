from rich import print
import os
from time import sleep


def limpar_tela() -> None:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

def formatar_mensagem_importante(cor: str, msg: str, tempo_espera: int = 2) -> None:
        print(f"[{cor}]{msg.upper()}[/]")
        sleep(tempo_espera)
