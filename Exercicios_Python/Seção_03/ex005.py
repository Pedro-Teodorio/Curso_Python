"""
    5 - Faça um programa que peça ao usuário para digitar 10 valores e some-os
"""
num = 1
soma = 0
while num <= 10:
    valores = int(input(f'Digite o Valor {num}/10: '))
    soma = valores + soma
    num = num + 1
print(f'A soma dos valores digitados foi {soma}')
