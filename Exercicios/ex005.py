"""

Iterando Strings com while

"""
contador_string = 0
nome = 'Victor Vahid'
tamanho_nome = len(nome)
novo_nome = ''
while contador_string < tamanho_nome:
    letra = nome[contador_string] 
    novo_nome += f' - {letra}'
    contador_string += 1

print(novo_nome)