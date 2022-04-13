"""
Saindo de Loops com break

Utilizamos o break para sair de loops de maneira projetada.
"""

# Exemplo 1

for num in range(1, 11):
    print(num)
    if num == 5:
        print('Chegou no 5 pare aqui')
        break
    else:
        print('Ainda não é o 5')
print('Saindo do loop')

# Exemplo 2

while True:
    comando = input('Digite sair para fechar o programa: ').lower()
    if comando == 'sair':
        break
