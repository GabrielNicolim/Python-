# Crie um programa que obtenha a largura e a altura de uma parede.
# Em seguida apresente suas dimensões e área
# e a quantidade de tinta necessária para pintar aquela parede

# 2m² = 1l de tinta

# Resposta:

largura = float(input('Largura da parede....: '))  # Obtem largura
altura = float(input('Altura da parede.....: '))  # Obtem altura

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².]'
      '\nPara pintar essa parede , você precisará de {}l de tinta'.format(largura, altura, (largura*altura), ((largura * altura) / 2)))
