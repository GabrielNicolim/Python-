from datetime import date

atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. ainda faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(atual+saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(atual - saldo))
