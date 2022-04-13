"""
    6 - Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
    assim como a diferença existente entre eles.
"""

num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))

if num1 > num2:
    diferenca = num1 - num2
    print(f'O número {num1} é o maior  e a diferença entre eles é de {diferenca}')
else:
    diferenca = num2- num1
    print(f'O número {num2} é o maior e a diferença entre eles é de {diferenca}')
