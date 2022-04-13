"""
    7 - Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
    números forem iguais imprima a mensagem 'Números iguais'
"""

num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))

if num1 > num2:
    print(f'O número {num1} é o maior')
elif num1 == num2:
    print('Os números são iguais')
else:
    print(f'O número {num2} é o maior')