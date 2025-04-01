import math

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro  # (x, y)
        self.raio = raio
    
    def area(self):
        return math.pi * (self.raio ** 2)
    
    def perimetro(self):
        return 2 * math.pi * self.raio
    
    def teste_pertencente(self, ponto):
        distancia = math.sqrt((ponto[0] - self.centro[0]) ** 2 + (ponto[1] - self.centro[1]) ** 2)
        return distancia <= self.raio

if __name__ == "__main__":
    c1 = Circulo((2,2), 3)
    print("Área:", c1.area())
    print("Perímetro:", c1.perimetro())
    print("Pertence ao círculo (0,0)?", c1.teste_pertencente((0,0)))
