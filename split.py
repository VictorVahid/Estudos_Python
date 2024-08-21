"""
split e join com list e str
split - divide uma string
join - une - uma string

"""

frase = ' Oha só que ,  coisa interessante'

lista_crua = frase.split(',')
print(lista_crua)

lista_frases = []
print(lista_frases)
for i, frase in enumerate(lista_crua):
    lista_frases.append(lista_crua[i].strip())

print("\nLista frase crua:\n",lista_crua) #Antes .strip
print("\nLista depois do .strip:\n",lista_frases)  #Depois .strip

frase_unidas = ','.join(lista_frases)
print("\nLista frase unidas:\n",frase_unidas)