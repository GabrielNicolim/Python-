resposta = input('Digite algo: ')

print('O Tipo primitivo desse valor é {0}'.format(type(resposta)))
print('É numérico? {0}'.format(resposta.isnumeric()))
print('É alfabético? {0}'.format(resposta.isalpha()))
print('É alfanumérico? {0}'.format(resposta.isalnum()))
print('É todo maiúsculo? {0}'.format(resposta.isupper()))
print('É todo minúsculo? {0}'.format(resposta.islower()))
print('Está capitalizado? {0}'.format(resposta.istitle()))  # Presença de maiúsculas e minúsculas
print('Só tem espaços? {0}'.format(resposta.isspace()))

