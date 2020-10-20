s = 0
for c in range(0, 6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        s += num
print('\n\033[33mA somas dos valores pares digitados é: ', s)
