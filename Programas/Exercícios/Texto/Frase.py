frase = str(input('Digite uma frase: ')).lower()
frase = frase.strip()

print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a') + 1))
print('A última letra A aparece na posição {}'.format(frase.rfind('a')+1))
