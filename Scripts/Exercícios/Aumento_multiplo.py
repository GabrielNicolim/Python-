salario = float(input('Qual seu salário? '))

if salario > 1250:
    aumento = salario*1.10
else:
    aumento = salario*1.15

print('Quem ganhava {:.2f} Passou a ganhar {:.2f}'.format(salario, aumento))
