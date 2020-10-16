peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual sua altura? (m) '))

imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}. Ela está '.format(imc))

if imc < 18.5:
    print('Abaixo do Peso')
elif imc < 25:
    print('na faixa do Peso Ideal')
elif imc < 30:
    print('na faixa do Sobrepeso')
elif imc < 40:
    print('na faixa da Obesidade')
else:
    print('na faixa da Obesidade Mórbida')