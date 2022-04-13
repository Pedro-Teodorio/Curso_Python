"""
6 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit
"""

temperatura = float(input('Temperatura atual em C°: '))

fahrenheit = temperatura * (9.0/5.0) + 32.0

print(f'A temperatura atual em Fahrenheit é : {fahrenheit}')
