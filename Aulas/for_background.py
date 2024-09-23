

texto = "Victor"  #Iteravel
iterador = iter(texto)  #Iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break


#A serie de  comando acima é oque o (for) faz
# 

for letra in texto:
    print(letra) 