"""
    6 - Faça um programa que leia 10 inteiros e imprima sua média.
"""

num = 1
soma = 0

while num <= 10:
    valores = float(input(f'Digite o Valor {num}/10: '))
    soma = soma + valores

    if num == 10:
        media = soma / num
        print(f'A média dos valores e de {media}')

    num = num + 1
