vel = int(input('Qual sua velocidade? '))

if vel <= 80:
    print('Tenha um bom dia! Dirija com segunrança')
else:
    print('MULTADO! Você excedeu o limite permitido de  80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format((vel-80)*7))
