s = 0  # Soma das idades
m_velho = ''
m_idade = 0
contf = 0
for p in range(0, 4):
    print('-' * 5, end='')
    print(' {}º PESSOA '.format(p + 1), end='')
    print('-' * 5)

    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: '))

    s += idade

    if m_idade < idade and sex == 'M':
        m_velho = nome
        m_idade = idade

    if idade < 20 and sex == 'F':
        contf += 1

print('A média das idades é {:.1f}'.format(s/4))
print('O homem mais velho tem {} anos e se chama {}'.format(m_idade, m_velho))
print('O número de mulheres com menos de 20 anos é {}'.format(contf))
