'''
lista_inteiros = [1, 2, -1, -2]

print(f"Exempplo de lista: {lista_inteiros}")

lista1 = [1, 2, 3, 4, -1, -2]
lista2 = list()

print(lista1)
print(lista2)

lista = ["Python", 1, True, False]

lista2 = list(lista)

print(lista2)


def list():
    vetor = [1, 2, 3, 4, 5]
    print(f'Exemplo de lista: {vetor}')

list()
n1 = int(input("Digite o valor 1: "))
n2 = int(input("Digite o valor 2: "))
n3 = int(input("Digite o valor 3: "))
n4 = int(input("Digite o valor 4: "))
n5 = int(input("Digite o valor 5: "))

lista = [n1, n2, n3, n4, n5]

print(lista)

lista = [1, 2, 3, 4, 5]

print(lista[-5])


lista = [2.0, "chicocunha", -2]

lista[2] = 1000

print(lista[2])
n1 = float(input("Digite o valor da nota 1: "))
n2 = float(input("Digite o valor da nota 2: "))
n3 = float(input("Digite o valor da nota 3: "))
n4 = float(input("Digite o valor da nota 4: "))
n5 = print("Media: " + str((n1 + n2 + n3 + n4)/4))

lista = [n1, n2, n3, n4]

print(lista)

def func(list1, list2):
    lista_soma = list1[0] + list2 [-1]
    print(f"A soma do valor do item do primeiro indice da primeira lista,\n"
          f"com o último item da segunda lista: {lista_soma}")

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

func(list1, list2)

lista = [1, 2, 3, 4, 5]

lista2 = lista[0:3:1]

lista3 = lista[0:4:1]

lista4 = lista[4:0:-1]

lista5 = lista[::-1]

lista6 = lista[:4]

print(lista6)


def inverte(param):
    return param[::-1]

print(inverte("127"))


def list_sum(x):
    listax = x + x
    print(listax)
x = [1, 2, 3]

list_sum(x)



def list(lista):
    print(lista)
    return lista[-1] + lista[-2] + lista[-3]
lista = [1, 2, 3, 4, 5]
print(f"A soma dos três últimos valores da lista = " + str(list(lista)))


lista1 = [5450, 2840, 4910, 8500, 5820]
def nasa_program(distance):
    nome_asteroide = input("Insira o nome do asteroide identificado: ")
    for distance in range(0, len(lista1)):
        print(f"O nome do asteroide: {nome_asteroide}")
        print(f"O valor da distância é: {lista1[distance]}km da terra")
dicionario1 = {"nome_asteroide": "lista1"}
nasa_program(lista)

'''


# Programa que mantem o registro da distância dos asteroides

while True:
    novoAsteroide = input("Existe mais asteroides para registrar? ")
    if novoAsteroide == 's':
        nome_asteroide = input("Insira o nome do asteroide identificado: ")
        n1 = float(input("Digite o valor da distance 1: "))
        n2 = float(input("Digite o valor da distance 2: "))
        n3 = float(input("Digite o valor da distance 3: "))
        n4 = float(input("Digite o valor da distance 4: "))
        n5 = float(input("Digite o valor da distance 5: "))
    else:
        break
    media = float((n1 + n2 + n3 + n4 + n5)/ 5)
    lista = [n1, n2, n3, n4, n5]
    D1 = {nome_asteroide:lista}
    print(D1)
    print(media)

#DESAFIO
player1 = input("Inserir nome:  ")
pontuacao1 = input("Inserir pontuação:  ")
player2 = input("Inserir nome:  ")
pontuacao2 = input("Inserir pontuação:  ")
player3 = input("Inserir nome:  ")
pontuacao3 = input("Inserir pontuação:  ")

dict = {
    player1: pontuacao1,
    player2: pontuacao2,
    player3: pontuacao3
}
a = 1
for item in sorted(dict, key= dict.get, reverse=True):
    print(f'O {a} primeiro colocado foi {item}, com {dict[item]}')
    a+=1


















