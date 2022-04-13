"""
    8 - Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido
"""
maior_numero = 0
menor_numero = 0
for indice in range(1, 10):

    valores = int(input(f'Digite um valor {indice}/10:'))

    if indice == 1:
        maior_numero = valores
        menor_numero = valores

    if valores > maior_numero:
        maior_numero = valores

    if valores < menor_numero:
        menor_numero = valores

print(f'O menor valor é {menor_numero}')
print(f'O maior valor é {maior_numero}')
