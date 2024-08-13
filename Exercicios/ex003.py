horas = input('Digite somente as horas atuais: ')

try:
    int_horas = int(horas)
    if(int_horas >= 0) and (int_horas <= 11):
        print('Bom dia')
    elif(int_horas >= 12) and (int_horas <=17):
        print('Boa tarde!')
    elif(int_horas >= 18)  and (int_horas <= 23):
        print('Boa noite!')
    else:
        print('Não conheço essa hora!')
except:
    print('Digite somente números inteiros!')