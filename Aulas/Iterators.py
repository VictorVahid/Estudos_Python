# Generator expression, Iterables e Iterators em Python

# Generator É UMA FUNÇÃO QUE PAUSA!
import sys as sys

iterable = ["Eu", "Tenho", "__iter__"]
iterator = iter(iterable)

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))  # <-Declaração do generator

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)
