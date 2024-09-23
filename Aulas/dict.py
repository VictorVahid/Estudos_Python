pessoa = {
    "nome": "Victor",
    "sobrenome": "Vahid",
    "idade": 18,
    "altura": 1.78,
    "endereco": [
        {"rua": "...", "numero": "123123"},
        {"rua": "...", "numero": "123123"},
    ],
}

# print(pessoa, type(pessoa))
print(pessoa["nome"])
print()
for chave in pessoa:
    print(chave, pessoa[chave])



