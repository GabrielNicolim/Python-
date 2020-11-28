# Crie um programa que receba 3 valores do tipo inteiro
# e retorne como resposta qual o maior e menor valor obtido

# Resposta:

a = int(input('Primeiro Valor...: '))
b = int(input('Segundo Valor....: '))
c = int(input('Terceiro Valor...: '))

# verifica quem é o menor

menor = a

if b < a and b < c:
    menor = b
else:
    if c < a and c < b:
        menor = c

# verifica quem é o maior

maior = a

if b > a and b > c:
    maior = b
else:
    if c > a and c > b:
        maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
