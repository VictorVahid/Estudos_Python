# Generator expression, Iterables e Iterators em Python

# Generator É UMA FUNÇÃO QUE PAUSA!
import sys

iterable = ["Eu", "Tenho", "__iter__"]
iterator = iter(iterable)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))  # <-Declaração do generator

# Diferença de Tamanho na Memória
# print(sys.getsizeof(lista))
# print(sys.getsizeof(generator))

# for n in generator:
#     print(n)


def generator(n=0):
    yield 1
    return "Acabou"
    yield 2
    return "Continuando..."
    yield 3
    return "Acabou!"


gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))
