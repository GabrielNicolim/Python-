# Exercício da OBI 2020 => Retirado de: https://neps.academy/problem/890

# Recebe valores de A, B e C

a = int(input())
b = int(input())
c = int(input())

if (b - a) == (c - b):  # Se estiverem a distância iguais
    print('0')
elif (b - a) < (c - b):  # Se C estiver mais distante que A
    print('1')
elif (b - a) > (c - b):  # Se A estiver mais distante que C
    print('-1')
