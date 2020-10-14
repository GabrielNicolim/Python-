# https://neps.academy/lesson/70

A, B = input().split()

A = float(A)
B = float(B)

M = (A+B)/2

if M >= 7:
    print('Aprovado')
elif M >= 4:
    print('Recuperacao')
else:
    print('Reprovado')
