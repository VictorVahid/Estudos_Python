# Try, Except, else e finally

# try:
#     a = 18
#     b = 0
#     c = a / b[0]
# except ZeroDivisionError:
#     print("Divisão por 0 \n")
# except NameError:
#     print("Nome b Não está definido")
# except Exception as error:
#     print("MSG: ", error)
# print("Continuar")


try:
    print("Abriu Arquivo!")
    8/0
except Exception as error:
    print("Error: ", error)
    print("Name: ", error.__class__.__name__)
else:
    print("NÃO DEU ERRO")
finally:
    print("Fechar Arquivo")
