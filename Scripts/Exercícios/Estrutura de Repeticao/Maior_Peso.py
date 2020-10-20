menor = 0
maior = 0

for p in range(0, 5):
    peso = float(input('Digite o {}° peso: '.format(p+1)))

    if p == 0:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso

print('\nO maior peso lido foi {:.1f} Kg'.format(maior))
print('O menor peso lido foi {:.1f} Kg'.format(menor))
