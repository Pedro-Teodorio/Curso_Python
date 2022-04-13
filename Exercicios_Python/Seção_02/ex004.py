"""
 4 - Faça um programa que leia um número e  caso ele seja positivo, calcule e mostre:
    - O número digitado ao quadrado
    - A raiz quadrada do número digitado
"""
import math

num = float(input('Digite um Número: '))

if num > 0:
    raiz = math.sqrt(num)
    quadrado = num ** 2
    print(f'A raiz quadrada de {num} é {raiz}')
    print(f'O quadrado do número {num} é {quadrado}')
else:
    print('Número Inválido')
