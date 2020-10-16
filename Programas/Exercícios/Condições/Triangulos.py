s1 = int(input('Primeiro Segmento..: '))
s2 = int(input('Segundo Segmento...: '))
s3 = int(input('Terceiro Segmento..: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos podem formar um triângulo ', end = '')

    if s1 == s2 == s3:  # Todos os lados iguais
        print('EQUILATERO')
    elif s1 != s2 != s3 != s1:  # Todos os lados diferentes
        print('ESCALENO')
    else:
        print('ISÓCELES') # Dois lados iguais
else:
    print('Os segmentos NÃO podem formar um triângulo')