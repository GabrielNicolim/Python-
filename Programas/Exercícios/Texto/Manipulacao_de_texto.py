frase = 'Curso em Vídeo Python'

print(frase)         # Apresenta toda a string
print(frase[::2])    # Apresenta frase de 2 em 2
print(frase.upper())  # Deixa tudo maiúsculo
print(frase.lower())  # Deixa tudo minúsculo
print('Número de O na frase: {}'.format(frase.count('o')))
print('Tamanho de frase: {}'.format(len(frase)))  # Retorna tamanho
frase = frase.replace('Python', 'Android')
print(frase)
