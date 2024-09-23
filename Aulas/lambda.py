"""
Introdução à função lambda (função anônima de uma linha)
   A função lambda é uma função como qualquer
   outra em Python. Porém, são funções anônimas
   que contém apenas uma linha. Ou seja, tudo
   deve ser contido dentro de uma única
   expressão.
lista = [
        {'nome': 'Luiz', 'sobrenome': 'miranda'},
        {'nome': 'Maria', 'sobrenome': 'Oliveira'},
        {'nome': 'Daniel', 'sobrenome': 'Silva'},
        {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
        {'nome': 'Aline', 'sobrenome': 'Souza'},
]
"""

# lista = [1, 23, 433, 12, 23, 123, 15, 78, 878, 9]
# lista.sort(reverse=True)
# print(lista)

lista = [
    {"nome": "Luiz", "sobrenome": "miranda"},
    {"nome": "Maria", "sobrenome": "Oliveira"},
    {"nome": "Daniel", "sobrenome": "Silva"},
    {"nome": "Eduardo", "sobrenome": "Moreira"},
    {"nome": "Aline", "sobrenome": "Souza"},
]

# Ordenar por Função
# def ordena(item):
#     return item["nome"]

# Ordenar por Lambda


# lista.sort(key=lambda item: item["nome"])
# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()


l1 = sorted(lista, key=lambda item: item["nome"])
l2 = sorted(lista, key=lambda item: item["sobrenome"])


# exibir(l1)
# exibir(l2)


# Lambda em
def executa(funcao, *args):
    return funcao(*args)


duplica = executa(lambda m: lambda n: n * m, 2)

print(duplica(5))

# Execução de lambda em 1 única linha de código
print(executa(lambda x, y: x * y, 2, 5))
print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
