# https://neps.academy/lesson/91

n = int(input())
correta = input()
candidato = input()

acertos = 0

for o, c in zip(correta, candidato):
    if o == c:
        acertos += 1

print(acertos)
