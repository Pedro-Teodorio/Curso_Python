"""
    9 - Faça um programa que leia um número inteiro. e depois imprima os N primeiros
    números naturais impares.
"""

valor_num = int(input('Digite um valor: '))
qtd_vezes = int(input('Quantidade de números impares a frente: '))

contador = 1

while contador <= qtd_vezes:

    valor_num = valor_num + 2
    print(valor_num)
    contador = contador + 1


