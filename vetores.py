from numpy import in1d


i1 = input("Informe a idade da pessoa: ")
a1 = input("Informe a altura da pessoa: ")
i2 = input("Informe a idade da pessoa: ")
a2 = input("Informe a altura da pessoa: ")
i3 = input("Informe a idade da pessoa: ")
a3 = input("Informe a altura da pessoa: ")
i4 = input("Informe a idade da pessoa: ")
a4 = input("Informe a altura da pessoa: ")
i5 = input("Informe a idade da pessoa: ")
a5 = input("Informe a altura da pessoa: ")

vet1 = [i1, i2, i3, i4, i5]
vet2 = [a1, a2, a3, a4, a5]

print(vet1)
print(vet2)

vet1[::-1] = vet1
vet2[::-1] = vet2

print(vet1)
print(vet2)