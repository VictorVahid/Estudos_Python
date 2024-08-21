"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html

"""
import decimal as dc

numero_1 = dc.Decimal(0.7)
numero_2 = dc.Decimal(0.5)

numero_3 = numero_1 + numero_2

print(numero_3) #Utilizando import decimal mostra o número com precisão maxima!
print(f'{numero_3:.2f}')
print(round(numero_3, 4))