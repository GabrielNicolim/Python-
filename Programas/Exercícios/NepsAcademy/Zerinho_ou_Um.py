# https://neps.academy/lesson/66

A, B, C = input().split()  # Entrada A , B , C

# .split => Utilizado junto do imput para distribuir os valores
# Obtidos na mesma linha entre as variáveis

# Conversão de valores para tipo int

A = int(A)
B = int(B)
C = int(C)

# Compara os valores obtidos

if A == B == C:  # Se todas iguais => Sem vencedor
    print('*')
elif A != B and B == C:  # Se A diferente => A é o vencedor
    print('A')
elif B != A and A == C:  # Se B diferente => B é o vencedor
    print('B')
elif C != B and B == A:  # Se C diferente => C é o vencedor
    print('C')
