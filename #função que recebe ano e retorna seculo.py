#função que recebe ano e retorna seculo

def seculo(ano):
    if 2001 <= ano <= 2100:
        print("XXI")
    elif 1901 <= ano <= 2000:
        print("XX")
    elif 1801 <= ano <= 1900:
        print("XIX")
    elif 1701 <= ano <= 1800:
        print("XVIII")
    elif 1601 <= ano <= 1700:
        print("XVII")
    elif 1501 <= ano <= 1600:
        print("XVI")
    elif 1401 <= ano <= 1500:
        print("XV")
    elif 1301 <= ano <= 1400:
        print("XIV")
    elif 1201 <= ano <= 1300:
        print("XIII")
    elif 1101 <= ano <= 1200:
        print("XII")
    elif 1001 <= ano <= 1100:
        print("XI")
    elif 901 <= ano <= 1000:
        print("X")
    elif 801 <= ano <= 900:
        print("IX")
    elif 701 <= ano <= 800:
        print("VIII")
    elif 601 <= ano <= 700:
        print("VII")
    elif 501 <= ano <= 600:
        print("VI")
    elif 401 <= ano <= 500:
        print("V")
    elif 301 <= ano <= 400:
        print("IV")
    elif 201 <= ano <= 300:
        print("III")
    elif 101 <= ano <= 200:
        print("II")
    elif 1 <= ano <= 100:
        print("I")
        

ano = int(input("Digite um ano: "))
    
data = seculo(ano)

