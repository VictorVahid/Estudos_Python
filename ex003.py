horas = input('Digite somente as horas atuais: ')

try:
    int_horas = int(horas)
    if(int_horas >= 0) and (int_horas <= 11):
        print('Bom dia')
    elif(int_horas >= 12) and (int_horas <=17):
        print('Boa tarde!')
    else:
        print('Boa noite!')
except:
    print('Digite SOMENTE as Horas')