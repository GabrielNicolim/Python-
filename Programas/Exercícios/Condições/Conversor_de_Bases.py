num = int(input('Digite um número inteiro: '))
print('''
Escolha uma das Bases de Conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL
''')

opc = int(input('\n=> '))

if opc == 1:
    print('O número {} em binário é {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('O número {} em octal é {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex(num)[2:]))
