print('\033[34m-=' * 17)
print('  Descubra se Seu Número é Primo')
print('-=' * 17)

num = int(input('\n\033[36mDigite um Número: '))
cont = 0  # Contador de Divisões

for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m{}'.format(c), end=' ')
        cont += 1
    else:
        print('\033[31m{}'.format(c), end=' ')

print('\n\n\033[36mO número {} foi divisível {} vezes'.format(num, cont))

if cont != 2:
    print('E por isso ele NÃO É PRIMO!')
else:
    print('E por isso ele É PRIMO!')
