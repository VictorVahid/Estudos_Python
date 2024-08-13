numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    if(numero_int % 2 == 0):
        print('Par')
    else:
        print('Impar')
except:
    print(f'{numero} não é um número inteiro!')
