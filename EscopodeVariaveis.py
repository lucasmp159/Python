"""
num = 1

def function (a):
    soma = a + num
    return soma

res = print(function(3))

ano = 2022
def voto(ano_nasc):
    calc_idade = ano - ano_nasc
    if calc_idade >= 18:
        print("Voto obrigatório")
    elif 16 <= calc_idade <= 17:
        print("Voto opcional")
    else:
        print("Voto negado")
    return calc_idade

resultado = voto(2004)


def fizz_buzz(a):
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    elif a % 5 == 0:
        print("Buzz")
    elif a % 3 == 0:
        print("Fizz")
    else:
        return a

res = fizz_buzz(3)
"""

def reverse (num):
    n1 = int(num[::-1])
    return n1

num = input("Digite um número inteiro: ")

resultado = reverse(num)

print(f"Valor invertido:{resultado}")