nome = str(input('Digite seu nome: '))
nome = nome.strip()  # Realiza uma remoção de espaços inúteis

nomeM = nome.upper()  # Torna maiúsculo
nomem = nome.lower()  # Torna minúsculo
nomeT = len(nome)  # Obtem tamanho
nomeP = nome.split()  # separa a string
nomePT = len(nomeP[0])

print("""
Analisando seu nome...

Seu nome em maiúsculo é {}
Seu nome em minúsculo é {} 
Seu nome tem ao todo {} letras
Seu primeiro nome é {} e ele tem {} letras
""".format(nomeM, nomem, nomeT, nomeP[0], nomePT))