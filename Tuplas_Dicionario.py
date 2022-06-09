"""
tupla = (1, 2.0, "hi", True)
print(tupla)


def function (tupla):
    print(f'Imprima essa tupla: {tupla}')
tup = (1, 2.0, "hi", True)
function(tup)

tupla = ([1, 2, 3], [4, 5, 6])

tupla[0][-1] = 100

print(tupla[0])

list_int = []

for index in range(0, 5):
    n = int(input("Digite um número inteiro: "))
    list_int += (n,)

print(list_int)


tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 'dez')

n = int(input("Digite um valor entre 0 e 10: "))

print(tupla[n])


palavras = ('DOING', 'EXERCISES', 'IS', 'THE', 'BEST', 'WAY', 'TO', 'LEARN')

palavra_lista = []

vogais = []

for palavra in palavras:
    for letra in palavra:
        if letra in 'AEIOU':
            palavra_lista.append(letra)


    for i in range(0, len(palavra_lista)):
        vogais.append(palavra_lista[i])

    palavra_lista = []
    print()

print(vogais)

tupla = ("Ola", "Mundo", 1, 2.0)

for value in tupla:
    print(value)

for index in range(0, len(tupla)):
    print(tupla[index])

def function (tupla, inteiro):
    print(tupla)
    count = tup.count(inteiro)
    print(f'O número {inteiro} foi contado {count} vezes')
tup = (1, 2, 3, 4, 1)
inteiro = int(input("Insira o número que será contado: "))

function(tup, inteiro)


times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR')

print(times[0:3])

print(times[-1])

print(times.index('Santos'))

agenda = {
    'nome': 'John Doe',
    'relefone': 99887798,
    'endereco': 'Rua qualquer coisa'
}

agenda.update({'peso': 90.0, 'idade': 21})

print(agenda)

nome = input("Digite o seu nome: ")
media = float(input("Digite a sua media: "))
situacao = ""

if media > 6:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperacao"
else:
    situacao = "Reprovado"

aluno = {
    'nome': nome,
    'media': media,
    'situacao': situacao
}

aluno = dict(nome=nome, media=media, situacao=situacao)

print(aluno)
"""
dic = {
    'nome': 'Lucas',
    'idade': 20
}

for chave in dic:
    print(dic[chave])

