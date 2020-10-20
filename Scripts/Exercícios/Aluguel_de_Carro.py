# 1 km = R$ 0.15
# 1 dia = R$ 60

dist = float(input('Km percorridos: '))
dia = int(input('Dias em que esteve com o carro: '))
print('Preço a pagar =  {:.2f}'.format((dia*60) + (dist*0.15)))
