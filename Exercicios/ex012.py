"""
    Crie uma Função que multiplica todos os argumentos
    não nomeados recebidos 
    Retorne o total para uma variável e mostre o valor
    da variável.
    Crie uma função fala se um número é par ou ímpar.
    Retorne se o número é par ou ímpar.
 """

def multiplica(*args):
    total = 1
    for numeros in args: 
        total *= numeros
    return total
    

resultado = multiplica(1,2,3,4,5)
print(resultado)
print(1*2*3*4*5)
print()

def parOuImpar(numero):
    resposta = numero % 2 == 0
    if resposta:
        return f'{numero} é par'
    return f'{numero} é ímpar'
    
print(parOuImpar(2))
print(parOuImpar(4))
print(parOuImpar(7))
print(parOuImpar(13))
print(parOuImpar(2831))

