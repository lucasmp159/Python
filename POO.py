"""
class Computador:
    def __init__(self, Modelo, Fabricante, Processador, MemoriaRam, TamanhoHD, OcuppiedSize, ligado):
        self.Modelo = Modelo
        self.Fabricante = Fabricante
        self.Processador = Processador
        self.MemoriaRam = MemoriaRam
        self.TamanhoHD = TamanhoHD
        self.OcuppiedSize = OcuppiedSize
        self.ligado = ligado

    def liga(self):
        Computador.ligado = True
        self.ligado = Computador.ligado

    def desliga(self):
        Computador.ligado = False
        self.ligado = Computador.ligado

    def limparHD(self, CleanSize):
        if 0 <= Computador.TamanhoHD <= 200:
            Computador.TamanhoHD = self.OcuppiedSize - CleanSize
        else:
            print("Não pode mais apagar memória")

    def ocuparhd(self, usedsize):
        if 0 <= self.TamanhoHD <= 200:
            self.TamanhoHD = self.OcuppiedSize + usedsize
        else:
            print("Não tem mais espaço no HD")

    def mostrar(self):
        print(self.TamanhoHD)


computador1 = Computador('Corsair', 'Galaxy', 'Intel Graphics', 8, 200, 50, True)
computador1.ocuparhd(50)
computador1.mostrar()


list_pc = []

for x in range (0, 6):
    Modelo = input("Digite o Modelo: ")
    Fabricante = input("Digite o Fabricante")
    
    list_pc.append(Computador(Modelo, Fabricante))

print(list_pc[1].Modelo)

for x in list_pc:
"""
#from pprint import pprint --> transforma em dicionário
class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo, vip):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.vip = vip

    def saque(self, valor_sacado):
        if self.saldo < valor_sacado:
            print("SALDO INSUFICIENTE")
        else:
            self.saldo -= valor_sacado

            return valor_sacado
    def deposito(self, valor_depositado):
        if valor_depositado < 0:
            print("VALOR A SER DEPOSITADO INFERIOR A ZERO")
        else:
            self.saldo += valor_depositado

            return valor_depositado



conta1 = ContaBancaria("Lucas", 123456, 1500, True)
print(vars(conta1)) #--> vars Transforma em dicionário


class carro:
    def __init__ (self, modelo, ano, velocidade, ligado):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        self.ligado = ligado

    def ligar(self):
        if self.ligado is True:
            print("O carro está ligado")
        else:
            print("O carro está desligado")

    def acelerar(self):
        if 0 <= self.velocidade <= 20:
            print("1 Marcha")
        elif 20 < self.velocidade < 30:
            print("2 Marcha")
        elif 30 < self.velocidade < 35:
            print("3 Marcha")
        elif 35 < self.velocidade < 45:
            print("4 Marcha")
        elif 45 < self.velocidade < 55:
            print("5 Marcha")

carro1 = carro("Tesla", 1994, 50, True)
carro1.ligar()
carro1.acelerar()


















