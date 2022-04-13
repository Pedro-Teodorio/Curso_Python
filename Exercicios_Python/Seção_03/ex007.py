"""
    7 - Faça um programa que leia 10 números inteiros positivos,ignorando os negativos,e imprima sua
    média
"""
soma = 0
for indice in range(1, 11):
    valores = float(input(f'Digite o Valor {indice}/10: '))

    if valores > 0:
        soma = valores + soma

    if indice == 10:
        media = soma / indice
        print(f'A média dos valores positivo é {media}')
