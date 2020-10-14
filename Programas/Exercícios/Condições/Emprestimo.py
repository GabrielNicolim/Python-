vc = int(input('Valor da Casa: R$'))
sc = int(input('Salário do Comprador: R$'))
a = int(input('Quantos Anos de Financiamento? '))

p = vc / (a*12)
p_min = sc * 0.3

print('Para Pagar Uma Casa de R${:.2f} em {} Anos a Prestação será de {:.2f}'.format(vc, a, p))

if p <= p_min:
    print('\nEmpréstimo pode ser CONCEDIDO!')
else:
    print('\nEmpréstimo NEGADO!')
