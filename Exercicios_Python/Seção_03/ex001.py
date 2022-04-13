"""
    1 - Faça um programa que determine ou mostre os cinco primeiros mútiplos de 3,
    considerando maiores que 0.
"""

num = int(input('Digite um Número: '))

for multiplos in range(1, 6):
    multi = num * multiplos
    print(f'{num} X {multiplos} = {multi}')

print(f'\nEsses são os 5 primeiros multíplos de {num}')
