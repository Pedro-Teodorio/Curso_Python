"""
    10 - Fça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal.
"""

sexo = input('Qual seu sexo ?\n(M) - Masculino\n(F) - Feminino\nSelecione um: ').upper()

if sexo == 'M':
    print('\nVocê é do sexo MASCULINO\n')
    altura = float(input('Qual sua altura ? '))
    calc_peso_ideal = (72.7 * altura) - 58
    print(f'Seu Peso ideal é : {calc_peso_ideal}')
elif sexo == 'F':
    print('\nVocê é do sexo FEMININO\n')
    altura = float(input('Qual sua altura ? '))
    calc_peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu Peso ideal é : {calc_peso_ideal}')
else:
    print('\nOPÇÃO INVALÍDA')
