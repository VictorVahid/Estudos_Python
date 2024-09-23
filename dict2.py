pessoa = {}

# Criar 'indice' dentro do dicionario
chave = "nome"
# acesso ao dicionario
pessoa[chave] = "Victor Vahid"
print(pessoa[chave])
# adição ao dicionario
pessoa["sobrenome"] = "Costa"
print(pessoa["sobrenome"])
# deletar um dicionario
del pessoa["sobrenome"]
print(pessoa)


#Get in dicionario
if pessoa.get("sobrenome") is None:
    print("Não existe")
else:
    print(pessoa["sobrenome"])
