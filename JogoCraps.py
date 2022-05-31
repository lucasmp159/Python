import random

def jogo_de_crap():
    while True:
        count = 0
        selecionado = 0
        dados = random.randint(2,12)
        if dados in [7, 12]:
            selecionado = dados
            print("natural " + str(selecionado))
            print("Ganhou")
            break
        if dados in [2, 3, 11]:
            count = 0
            selecionado = dados
            print("craps " + str(selecionado))
            print("Perdeu")
            break
        if dados in [4, 5, 6, 8, 9, 10]:
            count += 1
            selecionado = dados
            print("Ponto " + str(selecionado))
            if count > 0 and dados == 7:
                print("perdeu")
                break
            elif count > 0 and dados in [2, 3, 12]:
                print("perdeu")
                break
            elif dados != selecionado: 
                print("Jogue novamente")
            else:
                print("Ganhou repetindo o ponto")
                break
jogo_de_crap()
