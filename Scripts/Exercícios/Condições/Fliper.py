# https://neps.academy/lesson/69

P, R = input().split()  # split => Recebe na mesma linha

P = int(P)
R = int(R)

if P == 0:
    print('C')
elif R == 0:
    print('B')
else:
    print('A')
