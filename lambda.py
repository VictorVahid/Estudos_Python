salarios = [100, 200, 300, 400, 500]

# Uma variavel = uma lista(mapeamento de cada item(Função sem nome LAMBDA))
novos_salario = list(map(lambda x:x * 1.1, salarios))
print(novos_salario) 