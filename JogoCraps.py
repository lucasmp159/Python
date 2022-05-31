import random

def jogo_de_crap():
    while True:
        count = 0
        selecionado = 0
        dados = random.randint(2,12)
        if dados == 7 or dados == 11:
            selecionado = dados
            print("natural " + str(selecionado))
            print("Ganhou")
            break
        if dados == 2 or dados == 3 or dados == 12:
            count = 0
            selecionado = dados
            print("craps " + str(selecionado))
            print("Perdeu")
            break
        if dados == 4 or dados == 5 or dados == 6 or dados == 8 or dados == 9 or dados == 10:
            count += 1
            selecionado = dados
            print("Ponto " + str(selecionado))
            if count > 0 and dados == 7:
                print("perdeu")
                break
            elif count > 0 and (dados == 2 or dados == 3 or dados == 12):
                print("perdeu")
                break
            elif dados != selecionado: 
                print("Jogue novamente")
            else:
                print("Ganhou repetindo o ponto")
                break
jogo_de_crap()