# Crie um programa que obtenha o valor de duas notas (float) e retorne a média com 1 casa decimal

# Resposta:

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno : '))

print('\nA média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1, nota2, ((nota1+nota2)/2)))
