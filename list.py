"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append("Victor Vahid")
nome = lista.pop()
lista.append(12333)
del lista[-1]
# lista.clear()
lista.insert(0, 5)
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_a.extend(lista_b)
print(lista_a)


"""
Lista de listas e seus índices

"""


salas = [
    ["Maria","Helena",],

    ["Elaine",],

    ["Luiz","Flávio","Eduarda",],
    
    ]

for sala in salas: 
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
