nome  = input('Digite seu nome: ')
idade = input('Digite sua idade: ')


if(nome == '') or (idade == ''):
    print('Desculpe, você deixou campos vazios.')
else:
    print(f'seu nome é: {nome}')
    print(f'seu nome invertido é: {nome[::-1]}')
    if(' 'in nome):
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
