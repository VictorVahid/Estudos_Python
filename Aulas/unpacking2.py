"""
Desempacotamento  em chamdas
de métodos de funções

"""

string = 'ABCD'
lista = ['Maria', 1, 3, 4, 'Vahid', 'Theia']
tupla = ('python', 'é', 'legal')

salas = [
    ["Maria","Helena",],

    ["Elaine",],

    ["Luiz","Flávio","Eduarda",],
    
    ]

# a, *_, b,c = lista

# print(a,b,c, *_)

#Sobre iteráveis
# print(*lista)
# print('Maria', 1, 3, 4, 'Vahid', 'Theia')
# print(*string)
# print(*tupla)


print(*salas, sep='\n')