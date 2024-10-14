# copy, sorted, produtos.sort
# Exercícios
import copy

produtos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]


# Gere novos_produtos por deep copy (cópia profunda) ✅
novos_produtos = copy.deepcopy(produtos)

# Aumente os preços dos produtos a seguir em 10% ✅
for i in novos_produtos:
    i["preco"] *= 1.1

for produto in produtos:
    print(f"Produto: {produto['nome']}, Novo preço: R$ {produto['preco']:.2f}\n")

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)✅
produtosOrdenadosNome = copy.deepcopy(produtos)
# Ordene os produtos por nome decrescente (do maior para menor)✅
produtosOrdenadosNome.sort(key=lambda x: x["nome"], reverse=True)
print("\nOrdem Nome: ", produtosOrdenadosNome)


# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)✅
produtosOrdenadosPreco = copy.deepcopy(produtos)
# Ordene os produtos por preco crescente (do menor para maior)✅
produtosOrdenadosPreco.sort(key=lambda x: x["preco"])
print("\nOrdem preço: ", produtosOrdenadosPreco)


print("LISTA ORIGINAL: ", produtos)
