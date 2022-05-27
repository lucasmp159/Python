#função que recebe ano e retorna seculo

def int_to_roman(input):
     ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
     nums = ('M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
     result = []
 
     for i in range(len(ints)):
         count = int(input / ints[i])
         result.append(nums[i] * count)
         input -= ints[i] * count
     return ''.join(result)

def int_to_century(ano):
    seculo = int(ano / 100)
    resto = ano % 100
    if resto != 0:
        seculo = seculo + 1
    return int_to_roman(seculo)
    
print(int_to_century(1501))