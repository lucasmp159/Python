
vet1 = [1,2,3,4,5,6,7,8,9,10]
vet2 = [11,12,13,14,15,16,17,18,19,20]
print(vet1)
print(vet2)
vet3 = vet1 + vet2
vet3[::2] = vet1
vet3[1::2] = vet2 
print(vet3)