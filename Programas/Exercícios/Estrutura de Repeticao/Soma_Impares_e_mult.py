# Some todos os valores impares e multiplos de 3 entre 1 e 500

cont = 0
s = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1

print('A soma dos {} valores solicitados é {}'.format(cont, s))
