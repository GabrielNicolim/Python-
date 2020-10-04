import math
angulo = float(input('Digite o valor de um ângulo: '))
seno = math.sin(math.radians(angulo))
print('O Ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O Ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O Ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))