# Crie um programa que receba o valor do salário de uma pessoa

# Realize o aumento previsto:
# - Se o salário passar de 1250 => 10%
# - Do contrario => 15%

# Apresente o valor do salário após o aumento

# Resposta:

salario = float(input('Qual seu salário? '))

if salario > 1250:
    aumento = salario*1.10
else:
    aumento = salario*1.15

print('Quem ganhava {:.2f} Passou a ganhar {:.2f}'.format(salario, aumento))
