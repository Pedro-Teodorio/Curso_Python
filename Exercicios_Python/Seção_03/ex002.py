"""
    2 - Escreva um programa que escreva na de 1 a 100 ,de 1 em 1, 3 vezes. A primeira
    vez deve usar a estrutura de repetição for, a segunda while e a terceira while.
"""

num = 1

for contagem in range(1, 101):
    print(contagem)
    if contagem == 100:
        print('\nPrimeira Volta Acaba Aqui\n')
        while num <= 100:
            print(num)
            num = num + 1
            if num == 101:
                print('\nSegunda Volta Acaba Aqui\n')
                num = 1
                while num <= 100:
                    print(num)
                    num = num + 1

