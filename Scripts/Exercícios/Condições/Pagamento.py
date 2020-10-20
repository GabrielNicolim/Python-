print('\033[1;33m-=' * 20)
print('\t\t\tLojas Guanabara')
print('-=' * 20)
valor = float(input('\n\033[mDigite o Valor da Compra: \033[32mR$ '))

if valor > 0:
    print('''\033[1;34m
    [ 1 ] A Vista no Dinheiro (10% OFF)
    [ 2 ] A Vista no Cartão (5% OFF)
    [ 3 ] 2x no Cartão
    [ 4 ] 3x a 10x no Cartão 
    ''')

    opc = int(input('=> \033[m'))

    if opc == 1:
        pagar = (valor * 0.9)
        print('\nValor a ser pago: \033[32m R$ {:.2f}.'.format(pagar))
    elif opc == 2:
        pagar = (valor * 0.95)
        print('\nValor a ser pago: \033[32m R${:.2f}.'.format(pagar))
    elif opc == 3:
        pagar = (valor/2)
        print('\nValor a ser pago: \033[32m R${:.2f} \033[m em duas parcelas de \033[32m R${:.2f} \033[mSem juros'.format(valor, pagar))
    elif opc == 4:
        parcelas = int(input('\nEm Quantas parcelas deseja pagar? (3-10) '))

        if 11 > parcelas > 2:
            valor *= 1.20
            pagar = valor/parcelas
            print('\nValor a ser pago: \033[32m R${:.2f} \033[m em duas parcelas de \033[32m R${:.2f}'.format(valor, pagar))
        else:
            print('\n\033[31mValor Inválido')
    else:
        print('\n\033[31mValor Inválido')
else:
    print('\n\033[31mValor Inválido')