'''
arquivo = open('./arquivo.txt', 'r')

lines = arquivo.readlines(20)
print(lines)

for x in lines:
    print(x)

arquivo = open('./arquivo.txt', 'a')

arquivo.write('LINHA 1\n')

linhas = ['LINHA 1\n', 'LINHA 2\n', 'LINHA 3\n',]

arquivo.writelines(linhas)

def func(path):
    arquivo = open(path, 'r+')

    return arquivo.readlines()

lista = func('./arquivo.txt')

for linha in lista:
    print(linha)

arquivo = open ('./arquivo.txt', 'a')

def func(arquivo, linha):
    arquivo.write(linha + '\n')

while True:
    linha = input ("Digite o valor: ")

    func(arquivo, linha)

    code = input("Deseja continuar [s/n]: ")

    if code in 'Nn':
        break;
'''
# Extensao de um arquivo
from os.path import splitext

