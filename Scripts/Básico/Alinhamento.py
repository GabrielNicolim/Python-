nome = input('Qual seu nome? ')

print('Prazer em te conhecer {:^20} !'.format(nome))
# Centraliza em 20 espaços
print('Prazer em te conhecer {:>20} !'.format(nome))
# Alinha a direita utilizando 20 espaços
print('Prazer em te conhecer {:<20} !'.format(nome))
# Alinha a esquerda utilizando 20 espaços

print('Prazer em te conhecer {:=^20}'.format(nome))
# Centraliza utilizando 20 espaços e colocando = onde existir vazio

print('='*20)
# Apresenta = 20 vezes
