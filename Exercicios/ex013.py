def Multiplier_Creator(multiplier):
    def multiplicar(number):
        return number * multiplier

    return multiplicar


duplicar = Multiplier_Creator(2)
triplicar = Multiplier_Creator(3)
quadriplicar = Multiplier_Creator(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))
