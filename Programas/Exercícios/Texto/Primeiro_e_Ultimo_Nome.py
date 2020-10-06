nome = str(input('Digite seu nome: '))
nome = nome.strip()
dividido = nome.split()

print(""" 
Primeiro nome: {}
Ultimo nome: {}
""".format(dividido[0], dividido[(len(dividido)-1)]))
