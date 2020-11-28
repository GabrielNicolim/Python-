# Crie um programa que receba os valores dos segmentos de um triângulo e responda se os segmentos formam um triângulo

# Pesquise a fórmula :)

# Resposta:

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

r1 = float(input('Primeiro segmento...: '))
r2 = float(input('Segundo segmento....: '))
r3 = float(input('Terceiro segmento...: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos formam um triângulo!')
else:
    print('Os segmentos NÃO formam um triângulo')
