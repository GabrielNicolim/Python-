# https://neps.academy/lesson/78

n = int(input())

visualizacoes = []
for i in range(n):
    a = int(input())
    visualizacoes.append(a)

# Processamento

total = 0
resposta = -1

for i, v in enumerate(visualizacoes):  # Retorna índice para i e o valor indexado para v
    dia = i + 1
    total += v
    if total >= 1000000 and resposta == -1:
        resposta = dia

print(resposta)
