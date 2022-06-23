def sacar(cliente, valor):
    if not (cliente['saldo'] - valor <= 0):
        cliente['saldo'] -= valor

        return valor
    else:
        print("Saldo insuficiente!")

def depositar(cliente, valor):
    cliente['saldo'] += valor

    print("Valor depositado com sucesso!")

def mostrar_extrato(cliente):
    print(f"Seu saldo será {cliente} reais")

