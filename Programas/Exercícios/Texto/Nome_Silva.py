nome = str(input('Qual seu nome? '))
nome = nome.strip()
nome = nome.lower()

print('Seu nome têm Silva? {}'.format('silva' in nome))
