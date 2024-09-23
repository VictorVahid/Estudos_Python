"""

Interpolação básica de strings
s. - string
d e i - int
f. - float
x e X. - Hexadecimal (ABCDEF0123456789)

"""

nome  = 'Victor'
preco = 100.31232131
variavel = '%s, o preco é R$%.2f'  % (nome,preco)
print(variavel)
print('Valor de %d em hexadecimal é : %04x'  % (61,61)) 