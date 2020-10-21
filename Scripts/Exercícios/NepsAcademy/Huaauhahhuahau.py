risada = str(input())
risada_ve = ''  # Risada contendo apenas vogais Esquerda - Direita
risada_vd = ''  # Risada contendo apenas vogais Direita - Esquerda

for i in range(0, len(risada)):
    if risada[i] == 'a' or risada[i] == 'e' or risada[i] == 'i' or risada[i] == 'o' or risada[i] == 'u':
        risada_ve += risada[i]

for i in range(len(risada) - 1, -1, -1):
    if risada[i] == 'a' or risada[i] == 'e' or risada[i] == 'i' or risada[i] == 'o' or risada[i] == 'u':
        risada_vd += risada[i]

if risada_ve == risada_vd:
    print('S')
else:
    print('N')
