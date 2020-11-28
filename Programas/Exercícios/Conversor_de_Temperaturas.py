# Crie um programa que recebe um valor em °C e apresente sua conversão em °F

# Pesquise a fórmula :)

# Resposta:

tempC = float(input('Informe a temperatura em °C: '))  # Obtem temperatura em C°
tempF = ((9*tempC)/5)+32     # Converte temperatura para F
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(tempC, tempF))
