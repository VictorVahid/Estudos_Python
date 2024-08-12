nome = input('Digite seu nome: ')

try:
    if (len(nome)>1): 
        if(len(nome) <=4):
          print('Seu nome é curto!')
        elif(len(nome) >= 5) and (len(nome) <=6):
          print('Seu nome é normal!')
        else:
           print('Seu nome é muito grande!')
    else:
       print('Digite mais de uma letra!')
except:
    print('Ocorreu um erro, digite seu nome!')