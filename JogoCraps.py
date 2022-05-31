import random

def jogo_de_crap():
    while True:
        selecionado = 0
        dados = random.randint(2,12)
        print (dados)
        if dados in [7, 12]:
            print("natural " + str(dados))
            print("Ganhou")
            break
        if dados in [2, 3, 11]:
            print("craps " + str(dados))
            print("Perdeu")
            break
        if dados in [4, 5, 6, 8, 9, 10]:
            print("Ponto " + str(selecionado))
            if selecionado == dados:
                print("Ganhou repetindo o ponto")
                break
            else:
                selecionado = dados
                print("Jogue novamente")
               
jogo_de_crap()
