from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(ca, co)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))