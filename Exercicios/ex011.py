# cpf = input('digite seu cpf: ')

cpf_usuario = '118.496.420-36'
#Tratamento de CPF
cpf_usuario = cpf_usuario.replace('.','')
cpf_usuario = cpf_usuario.replace('-','')

#Primeiro DIGITO CPF
noveDigitos = cpf_usuario[:9]
contador_regressivo_1 = 10

resultado_digit_1 = 0
for digito in noveDigitos:
    resultado_digit_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
firstDigit = (resultado_digit_1 * 10) % 11

firstDigit = firstDigit if firstDigit <= 9 else 0


#Segundo DIGITO CPF
dezDigitos = noveDigitos + str(firstDigit)
contador_regressivo_2 = 11

resultado_digit_2 = 0

for digito in dezDigitos:
    resultado_digit_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -=1
secondDigit = (resultado_digit_2 * 10) % 11
secondDigit = secondDigit if secondDigit <= 9 else 0



novoCPF= f'{noveDigitos}{firstDigit}{secondDigit}'


if cpf_usuario == novoCPF:
    print(f'O {cpf_usuario} é válido!')
else:
    print('CPF INVÁLIDO!')