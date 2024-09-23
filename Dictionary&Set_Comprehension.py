# Dictionary Comprehension

produto = {
    "nome": "caneta azul",
    "preco": 2.5,
    "categoria": "Escritorio",
}

dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != "categoria"
}

print(dc)

# Set comprehesion
s1 = {i for i in range(11)}
print(s1)
