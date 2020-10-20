num = int(input('Digite um número: '))
n = str(num)

u = num // 1 % 10    # Unidade
d = num // 10 % 10   # Dezena
c = num // 100 % 10  # Centena
m = num // 1000 % 10 # Milhar

print("""
Analisando o número {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
""".format(n, u, d, c, m))
