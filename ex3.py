import math
import datetime

class Funcionario:
    def __init__(self, id, sobrenome, nome, nascimento, admissao, salario):
        self.id = id
        self.sobrenome = sobrenome
        self.nome = nome
        self.nascimento = nascimento
        self.admissao = admissao
        self.salario = salario

    def idade(self):
        ano_atual = datetime.datetime.now().year
        return ano_atual - self.nascimento[2]

    def tempo_de_casa(self):
        ano_atual = datetime.datetime.now().year
        return ano_atual - self.admissao[2]   

    def aumento_de_salario(self):
        anos = self.tempo_de_casa()
        if anos < 5:
            self.salario *= 1.02
        elif anos < 10:
            self.salario *= 1.05
        else:
            self.salario *= 1.10 
    
if __name__ == "__main__":
    emp = Funcionario('007', 'Bond', 'James', (11,11,1970), (7,4,1995), 7500)
    emp.aumento_de_salario()
    print("Idade:", emp.idade())
    print("Tempo de casa:", emp.tempo_de_casa())
    print("Salário atualizado:", emp.salario)