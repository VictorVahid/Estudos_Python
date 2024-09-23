"""
Introdução à List comprehension em Python
List comprehension é uma forma rápida para criar listas
a partir de iteráveis.

"""

import pprint


def p(v):
    pprint.pprint(
        v,
        indent=3,
        width=60,
        depth=2,
        compact=True,
        sort_dicts=False,
        underscore_numbers=False,
    )


# Sem a utilização de List Comprehension

lista = []

for numero in range(11):
    lista.append(numero * 2)
# print("Sem List Comprehension: ", lista)

# Com a utilização de List Comprehension

lista = [numero * 2 for numero in range(11)]
# print("Com List Comprehension: ", lista)

# Mapeamentos de dados List Comprehension (Inclusão de dados)
produtos = [
    {
        "nome": "p1",
        "preco": 20,
    },
    {
        "nome": "p2",
        "preco": 10,
    },
    {
        "nome": "p3",
        "preco": 30,
    },
]

# Map (Inlcluir dados)
novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
    for produto in produtos
    if (produto["preco"] >= 20)
    and (produto["preco"] * 1.05 > 10)  # Filtro (Excluir ou limitar saida)
]
# p(novos_produtos)

# Filtro em List Comprehension

listaFiltro = [n for n in range(11) if n < 6]
# print(listaFiltro)

list = []
# for x in range(3):
#     for y in range(3):
#         list.append((x, y))
list = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]

p(list)
