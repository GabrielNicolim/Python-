salario = float(input('Qual o salário do funcionário? R$'))
aumento = int(input('Quanto deve aumentar o salário[%]? '))
print('Um funcionário que ganhava R${:.2f}, com aumento de {}%, passa a receber R${:.2f}'.format(salario, aumento, (salario + (salario*(aumento/100)))))
