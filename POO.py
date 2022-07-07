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
            print("SALOD INSUFICIENTE")
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

