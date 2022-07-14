"""
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.idade = idade

    @property
    def get_nome(self):
        return self.__nome

    @get_nome.setter
    def set_nome(self, nome):
        self.__nome = nome

pessoa1 = Pessoa("Joph", 40)

pessoa1.idade = ""

print(pessoa1.get_nome)
pessoa1.set_nome = "Uris"
print(pessoa1.get_nome)


from typing_extensions import Self


class Carro:
    def __init__(self, marca, cor, velocidade):
        self.__marca = marca
        self.__cor = cor
        self.__velocidade = velocidade

    @property
    def get_marca(self):
        return self.__marca

    @get_marca.setter
    def set_marca(self, marca):
        self.__marca = marca

    @property
    def get_cor(self):
        return self.__cor

    @get_cor.setter
    def set_cor(self, cor):
        self.__cor = cor

    @property
    def get_velocidade(self):
        return self.__velocidade

    @get_velocidade.setter
    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade


    def acelerar(self, acelera):
        acelera = self.velocidade + 10
        if  acelera > 190:
            self.__velocidade
            print("Não pode mais acelerar")
        else:
            self.__velocidade += 10
            print("Acelerou")

    def frear(self, freio):
        freio = self.velocidade - 10
        if freio < 10: 
            self.__velocidade = freio           
            print("Não pode Freiar")
        else:
            self.__velocidade -= 10
    

carro1 = Carro("Tesla", "Branco", 180)
print(carro1.get_velocidade)
print(carro1.acelerar(carro1.get_velocidade))


class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self,idade):
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf


p = Pessoa("Uris", 40, "1232121")

print(p.nome)


class Pessoa:
    nome = ""

    def falar(self):
        print("Falei")

class Funcionario(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

f = Funcionario()

f.falar()

f.trabalhar()
"""
class Funcionarios:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario

class Estagiario(Funcionario):
    def __init__(self, matricula, nome, salario):
        super().__init__(matricula, nome, salario)

class Gerente(Funcionarios):
    def __init__(self, matricula, nome, salario):
        super().__init__(matricula, nome, salario)

e = Estagiario("123", "Lucas", 2000)