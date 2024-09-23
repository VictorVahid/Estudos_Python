a, b = 1, 2
a, b = b, a
# print(a, b)  # Isso vai imprimir: 2 1

pessoa = {
    "nome": "Victor",
    "sobrenome": "Vahid",
}
dados_pessoa = {
    "idade": 19,
    "altura": 1.76,
}

# Empacotamento e Desempacotamento de Dicionários
# Loop para imprimir chaves e valores
# for chave, valor in pessoa.items():
#     print(f"Chave: {chave}, Valor: {valor}")

# Combinação de dicionários
pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# Desempacotamento de valores e itens
a, b = pessoa.values()
# print("Valores:", a, b)

itens = list(pessoa.items())
# print("Itens:", itens)


# args e kwargs
# kwargs - key arguments(Argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print("NÃO NOMEADOS: ", args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(1, 2, 3, nome="Victor", sobrenome="Vahid")


# Desempacotamento de dicionarios em funcao
mostro_argumentos_nomeados(**pessoa_completa)

# Exemplos
config_computador = {
    "processador": {
        "marca": "Intel",
        "modelo": "Core i7-13700K",
        "frequencia_base_ghz": 3.4,
        "nucleos": 8,
        "threads": 16,
    },
}

mostro_argumentos_nomeados(**config_computador)
