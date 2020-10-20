# 1 USD = R$ 5.61

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.61
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
