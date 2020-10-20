# 2m² = 1l de tinta

largura = float(input('Largura da parede....: '))  # Obtem largura
altura = float(input('Altura da parede.....: '))  # Obtem altura

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².]'
      '\nPara pintar essa parede , você precisará de {}l de tinta'.format(largura, altura, (largura*altura), ((largura*altura)/2)))
# Apresenta a resposta final
