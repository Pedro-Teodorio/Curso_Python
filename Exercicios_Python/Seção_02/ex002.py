"""
    2 - Leia um número fornecido pelo usuário.Se esse número for positivo, calcule a raiz
    quadrada dele.Se o número for negativo, mostre a mensage dizendo que o número é inválido.
"""
import math

num = float(input('Digite um Número: '))

if num > 0:
    raiz = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {raiz}')
else:
    print('Número Inválido')
