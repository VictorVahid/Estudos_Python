# raise - Lançando exceções (errors)


def Verificar_Entrada(a, b):
    if a == 0 or b == 0:
        raise ZeroDivisionError("Você está tentando Dividir por ZERO")
    return True


def TypeVerify(a, b):
    if not isinstance(a, b(float, int)):
        raise TypeError("Erro de tipo")
    return True


def divisão(a, b):
    TypeVerify(a, b)
    # Verificar_Entrada(a, b)

    return a / b


print(divisão(2, "2"))
