# + => Adição
# - => Subtração
# * => Multiplicação
# / => Divisão
# ** => Potência
# // => Divisão inteira
# % => Resto da divisão

n1 = int(input('Um valor.........: '))
n2 = int(input('Outro valor......: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}.'.format(s, m, d), end='')
print(' Divisão inteira {} e potência {}'.format(di, e))

# {:.3f} => Define que o valor terá 3 casas decimais
# end = x => x será realizado ao término do print
