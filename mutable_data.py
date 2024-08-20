"""
Cuidados com dados mutáveis
=- copiado o valor (imutáveis)
=- aponta para o mesmo valor na memória (mutável)

"""

lista_a = ['Victor', 'Vahid']
lista_b = lista_a.copy()

lista_a[1] = 'Mahid'

print(lista_a)
print(lista_b)