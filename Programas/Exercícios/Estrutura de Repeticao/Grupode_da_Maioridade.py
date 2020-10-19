from datetime import date  # Obtem func date de datetime

atual = date.today().year  # Obtem o ano atual
cont_ma = 0  # Contador de maiores de idade
cont_me = 0  # Contador de menores de idade

for c in range(0, 7):
    aux = int(input('Em que ano a pessoa {} nasceu? '.format(c+1)))
    idade = atual - aux  # Obtem a idade da pessoa no ano atual

    if idade >= 21:  # Checa se é maior de idade
        cont_ma += 1
    else:
        cont_me += 1

print('\nAo todo tivemos {} pessoas maiores de idade'.format(cont_ma))
print('E também tivemos {} pessoas menores de idade'.format(cont_me))

