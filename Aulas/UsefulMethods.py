# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    "nome": "Victor",
    "sobrenome": "Vahid",
}
# len
print("# len")
print(len(pessoa))
print()

# keys
print("# keys")
print(tuple(pessoa.keys()))
print()

# values
print("# values")
print(tuple(pessoa.values()))
print()

# items
print("# items")
print(tuple(pessoa.items()))
print()

# setdefault
print("# setdefault")
pessoa.setdefault("idade", 0)
print(tuple(pessoa.items()))
print()

# copy (Copia Rasa)
d1 = {
    "c1": 1,
    "c2": 2,
    "l1": [0, 1, 2],
}

# A copia vai afetar as 2 listas, para não ter esse problema usa-se `copy.deep.copy()`
d2 = d1.copy()
d2["c1"] = 1000
d2["l1"][1] = 99999
print("# copy `Copia Rasa`")
print(d1)
print(d2)
print()

# get (PADRAO: None)
print("# get")
print(pessoa.get("altura", "Não existe"))
print(pessoa.get("nome"))
print()

# pop
print("# pop")
nome = pessoa.pop("nome")
print(nome)
print(pessoa)
print()

# popitem
print("# popitem")
last_key = pessoa.popitem()
print(last_key)
print(pessoa)
print()

# update
print("# update")
# Primeira forma de usar update
pessoa.update({"altura": 1.78, "nome": "Maria"})
print(pessoa)
# Segunda forma de usar update
pessoa.update(sobrenome="elis", idade=20, altura=1.53)
print(pessoa)
# Terceira forma de usar update
tupla = (("nome", "novo valor"), ("idade", 21))
lista = [["nome", "new value"], ["idade", 22]]
pessoa.update(tupla)
print("Tupla: ")
print(pessoa)
print("Lista: ")
pessoa.update(lista)
print(pessoa)
