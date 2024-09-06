# Set - Conjuntos em Python(tipo set)
s1 = set()  # Set vazio
s2 = {"Luiz", 1, 2, 3, 3, 3, 3, 3, 3}  # Set com dados
print(s1, s2, sep="|")

for i, item in enumerate(s2):
    print(item)

# Conversão de lista para SET e Remoção de iteraveis repetidos
lista = [1, 2, 3, 4, 5, 1, 2, 2, 3, 1, 2, 3, 5, 2, 2, 1, 3]
set_lista = set(lista)
lista_2 = list(set_lista)
print(lista_2)


"""
 - Sets são eficientes para remover valores duplicados de iteráveis.
 - Seus valores serão sempre únicos;
 - Não aceitam valores mutáveis;
 - não tem índexes;
 - não garantem ordem;
 - são iteráveis (for, in, not in)

    Operadores úteis:
     união | união (union) - Une
     intersecção & (intersection) - Itens presentes em ambos
     diferença - Itens presentes apenas no set da esquerda
     diferença simétrica ^ - Itens que não estão em ambos

 - Métodos úteis:
    add, update, clear, discard

"""
