"""
    3 - Leia um número real. Se o número for positivo imprima a raiz quadrada.Do contrário
    imprima o número ao quadrado
"""
import math

num = float(input('Digite um número :'))

if num > 0:
    raiz = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {raiz}')
else:
    quadrado = num ** 2
    print(f'O quadrado do número {num} é {quadrado}')
