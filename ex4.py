import math
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if valor > self.__saldo:
            print("Erro: Saldo insuficiente!")
        else:
            self.__saldo -= valor
    
    def exibir_saldo(self):
        return self.__saldo

if __name__ == "__main__":
    c1 = ContaBancaria("Alice", 1000)
    c1.depositar(500)
    print("Saldo após depósito:", c1.exibir_saldo())
    c1.sacar(2000)
    c1.sacar(300)
    print("Saldo final:", c1.exibir_saldo())
