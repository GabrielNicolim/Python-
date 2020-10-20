# Crie um programa que recebe uma quantidade de reais e retorne esse valor convertido em dólar

# Considere 1 USD = R$ 5.61

# Resposta:

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.61
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
