frase = str(input('Digite uma Frase: ')).strip().upper()
palavras = frase.split()  # Sepera em uma lista
junto = ''.join(palavras)  # Reagrupa as palavras
inverso = ''

inverso = junto[::-1]

'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''

if inverso == junto:
    print('\033[32mTemos um Palíndromo!')
else:
    print('A Frase Digitada \033[32mNÃO É UM PALÍNDROMO')
