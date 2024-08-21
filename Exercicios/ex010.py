import os

lista = []
valor = ""
while True:
    print("Selecione uma opção")
    entrada = input("[i]nserir [a]pagar [l]istar [s]air: ").lower()

    # Validação
    if len(entrada) > 1:
        print("Digite apenas uma letra.")

    #Entrada Usuario
    if entrada == "i":
        os.system("cls")
        valor = input("Valor: ")
        lista.append(valor)
    
    if entrada == "a":
        print(lista)
        indice = int(input("Escolha o índice para apagar: "))
        try:
            lista.pop(indice)
            print(f"O item {indice} foi removido.")
        except IndexError:
            print("Índice inválido. Tente novamente.")
   
    if entrada == "l":
        for indice, nome in enumerate(lista):
            print(indice, nome)
        
    # Saida
    if entrada == "s":
        print("Saindo do programa...")
        break
