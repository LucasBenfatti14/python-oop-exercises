from transportes import Transporte, Moto, Drone, Caminhao


def main():
    dist = 20

    entrega = Moto(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}")


if __name__ == "__main__":
    main()