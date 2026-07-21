from rich import print, inspect
from classes import Poligono, Circulo, Quadrado

def main():
    q = Quadrado(12)

    print(f"Perímetro = {q.perimetro():.1f}")
    print(f"Área = {q.area():.1f}")
    inspect(q, methods=True)

if __name__ == "__main__":
    main()