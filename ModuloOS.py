
"""
print(os.name)

print(os.getcwd())

os.chdir('../')

print(os.getcwd())

os.mkdir('./folder123')

print(os.getcwd())


from os.path import isfile, isdir

print(isfile('./main2.py'))

print(isdir('./folder'))


#os.rmdir('./folder123')

import shutil

# Serve para apagar uma pasta com conteúdo dentro.
# shutil.rmtree('./folder')

# Serve para apagar arquivos.
os.remove('./texto.txt')

origem = './modulo1.py'
dest = './rebanedmodule.py'

os.rename(origem, dest)


def teste():
    import os
    teste1 = os.path.isdir('./folder')
    if teste1 == True:
        print("A pasta existe")
    else:
        print("A pasta não existe")
    teste2 = os.path.isfile('./folder/texto.txt')
    if teste2 == True:
        print("O arquivo existe")
    else:
        print("O arquivo não existe")
teste()

from os.path import isfile, isdir
def func(path, option):
    if option == 'file':
        return isfile(path)
    else:
        return isdir(path)

print(func('./main.py', 'file'))

from os import rename, getcwd

def func(origem, dest):
    print(getcwd())
    rename(origem, dest)
func('./rebanedmodule.py', './exerM01.py')
"""
