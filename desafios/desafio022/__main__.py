from rich import print
from funcoes import (limpar_tela, formatar_mensagem_importante)
from controle_remoto import ControleRemoto

def main():
    controle = ControleRemoto()
    while True:
        limpar_tela()
        print(controle.mostrar_tv())
        comando = controle.comando_controle()
        if comando == "@":
            controle.ligar_desligar_tv()
        if comando == "0":
            break
        if controle.tv_ligada:
            match comando:
                case "@":
                    pass
                case "+":
                    controle.aumentar_volume()
                case "-":
                    controle.diminuir_volume()
                case ">":
                    controle.avancar_canal()
                case "<":
                    controle.voltar_canal()
                case _:
                    formatar_mensagem_importante("red","erro! comando inválido!")
                    continue
    formatar_mensagem_importante("yellow","saindo da sala de estar...")

if __name__ == "__main__":
    main()
