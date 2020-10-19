print('\033[33m=-=' * 8)
print('  10 Termos de uma PA')
print('=-=' * 8)
primeiro = int(input('\033[mDigite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 * razao)

for c in range(primeiro, decimo, razao):
    print('{} '.format(c), end='>> ')
print('ACABOU')
