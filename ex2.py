import math

class Domino:
    def __init__(self, lado_a=0, lado_b=0):
        self.lado_a = lado_a
        self.lado_b = lado_b
    
    def mostrar_pontos(self):
        print(f"Lado A: {self.lado_a} | Lado B: {self.lado_b}")
    
    def valor(self):
        return self.lado_a + self.lado_b

if __name__ == "__main__":
    d1 = Domino(2,6)
    d2 = Domino(4,3)
    d1.mostrar_pontos()
    d2.mostrar_pontos()
    print("Total de pontos:", d1.valor() + d2.valor())
