
"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

"""

def soma(x, y, z= None):
    #Definição
    if z is not None:
        print(f'{x = } { y = } { z = }', '|','x + y + z = ', x + y + z)
    else: 
        print(f'{x = } { y = }', '|','x + y = ', x + y)

soma(3,6)
soma(y=61,z=55,x=3)




