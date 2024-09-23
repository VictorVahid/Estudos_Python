
def soma (*args):
   total = 0
   for numeros in args:
    total += numeros
   return total


numeros = 1 ,2,3,4,5,6,78,8,9,12
outra_som = soma(*numeros)
print(numeros)
soma_1_2_3 = soma(1,2,3)
# print(soma_1_2_3)
soma_4_5_6 = soma(4,5,6)
# print(soma_4_5_6)
print(outra_som)

# print(sum((12,123,123,123,54,123,123,3)))