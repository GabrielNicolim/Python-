num1 = int(input('Digite um número.....: '))
num2 = int(input('Digite outro número..: '))

if num1 == num2:
    print('Os valores são iguais')
elif num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num1 < num2:
    print('{} é maior que {}'.format(num2, num1))
