from datetime import date

atual = date.today().year

nasc = int(input('Digite seu ano de nascimento: '))

idade = atual - nasc

print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
