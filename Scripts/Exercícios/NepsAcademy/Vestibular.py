# Exercício retirado de https://github.com/GabrielNicolim/Estudo_C/tree/master/Programas/Exerc%C3%ADcios_02

n = int(input())
correta = input()
candidato = input()

acertos = 0

for o, c in zip(correta, candidato):
    if o == c:
        acertos += 1

print(acertos)
