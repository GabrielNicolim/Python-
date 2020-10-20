from math import floor, ceil  # Importa duas funções de math
num = float(input('Digite um número: '))
print('{:.2f} arredondado para cima é {:.2f}'.format(num, ceil(num)))
print('{:.2f} arredondado para baixo é {:.2f}'.format(num, floor(num)))
