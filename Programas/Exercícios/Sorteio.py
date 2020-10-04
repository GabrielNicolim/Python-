from random import choice
# Importa apenas choice da biblioteca random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
# choice => Escolhe um valor aleatório em uma lista
print('O aluno escolhido foi {}'.format(escolhido))
