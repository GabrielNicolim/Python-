n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

me = (n1+n2)/2

print('Quem tirou {:.1f} e {:.1f} tem média {:.1f}'.format(n1, n2, me))

if me >= 7:
    print('O aluno foi aprovado!')
elif me >= 5:
    print('O aluno está de recuperação')
else:
    print('O aluno foi reprovado')
