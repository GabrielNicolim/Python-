from random import randint
from time import sleep

aleatorio = randint(0, 5)
# Escolhe um número entre 0 e 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-' * 20)
palpite = int(input('Em qual número eu pensei? '))
# Jogador tenta adivinhar

print('PROCESSANDO...')
sleep(3)

if aleatorio == palpite:
    print('PARABÉns! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(aleatorio, palpite))
