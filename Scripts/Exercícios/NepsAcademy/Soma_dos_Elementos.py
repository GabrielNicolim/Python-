# Exercício retirado de: https://neps.academy/lesson/84

n = int(input())
v = input().split()  # Armazena todos os valores adicionados na linha em lista
s = 0

for i in range(len(v)):  # Realiza a soma dos valores da lista
    s += int(v[i])

print(s)
