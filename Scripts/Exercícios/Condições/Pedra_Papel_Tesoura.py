from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''\033[34mSuas opções

[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')

jogada = int(input('Qual sua jogada? '))

print('\n\033[32mJo')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\n')
sleep(1)

if 2 >= jogada >= 0:
    print('\033[33m-=' * 15)
    print('Computador Jogou {}'.format(itens[computador]))
    print('Jogador Jogou {}'.format(itens[jogada]))
    print('-=' * 15)

    print('\n\033[32m')

    if computador == 0:  # PEDRA
        if jogada == 0:
            print('EMPATE')
        elif jogada == 1:
            print('O Jogador GANHOU!')
        elif jogada == 2:
            print('O Jogador PERDEU :(')
    elif computador == 1:  # PAPEL
        if jogada == 0:
            print('O Jogador PERDEU :(')
        elif jogada == 1:
            print('EMPATE')
        elif jogada == 2:
            print('O Jogador GANHOU!')
    elif computador == 2:  # TESOURA
        if jogada == 0:
            print('O Jogador GANHOU!')
        elif jogada == 1:
            print('O Jogador PERDEU :(')
        elif jogada == 2:
            print('EMPATE')
else:
    print('\033[31m Jogada Inválida')