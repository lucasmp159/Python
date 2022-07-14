'''
def func(msg, msg2):
    print(msg, msg2)

func("Olá", True)

def procedure(msg):
    print(msg)

procedure("Hello World!")

def area(largura,comprimento):
    resultado = print(largura * comprimento)
    return resultado

area(10, 20)

def maior_menor(num1, num2):
    if num1 < num2:
        print("{} Maior que o {}".format(num2,num1))
    elif num1 > num2:
        print("{} Menor que o {}".format(num2, num1))
    else:
        print("Eles são iguais")
    return maior_menor

maior_menor(5, 6)
'''
def comp(a, b, c):
    soma = a + b
    if soma < c: 
        return True
    else:
        return False


res = comp(1, 2, 3)

def sayHello(msg):
    return f"Sua mensagem é: {msg}"

msg = input("Digite uma mensagem: ")

myMsg = sayHello(msg)

print(msg)
