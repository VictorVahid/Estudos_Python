# Set - Conjuntos em Python(tipo set)
set1 = set()  # Set vazio
set2 = {"Luiz", 1, 2, 3, 3, 3, 3, 3, 3}  # Set com dados
# print(set1, set2, sep="|")

# for i, item in enumerate(set2):
#     # print(item)

# Conversão de lista para SET e Remoção de iteraveis repetidos
# lista = [1, 2, 3, 4, 5, 1, 2, 2, 3, 1, 2, 3, 5, 2, 2, 1, 3]
# set_lista = set(lista)
# lista_2 = list(set_lista)
# # print(lista_2)


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

s1 = set()
s1.add("Victor")
s1.add(1)
s1.update(("Olá mundo", 1, 2, 3, 4))  # Adição de forma Iterada
# s1.clear()
s1.discard("Olá mundo")  # Passa o próprio valor para remover do set
# print(s1)


"""

- Operadores úteis:
- união [|] união (union) - Une
- intersecção [&] (intersection) - Itens presentes em ambos
- diferença[-] Itens presentes apenas no set da esquerda
- diferença simétrica [^] - Itens que não estão em ambos

"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2

# print(s3)

# Exemplo de uso dos sets
letras = set()
while True:
    letra = input("Digite: ")
    letras.add(letra.lower())

    if "l" in letras:
        print("Parabéns")
        break
    print(letras)
