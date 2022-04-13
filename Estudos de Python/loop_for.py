"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

Python
for item in iteravel:
    //execução do loop

Utilizamos loops para iterar sobre sequẽncias ou sobre valores iteráveis

Exemplos de iteraveis?

- String
    nome = 'Pedro Lucas'
- Lista
    lista = [1, 2, 3]
- Range
    numeros =  range(1, 10)

//////////////////////////////////////////////////////////////////////

# Exemplo for 1 (Iterando sobre uma string)
for letra in nome:
    print(letra,"\n")

# Exemplo for 2 (Iterando sobre lista)
for numero in lista:
    print(numero, "\n")

# Exemplo for 3 (Iterando sobre um  range)
range(valor_inicial, valor_final)
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
    print(numero)

# Enumerate
for indice in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descarta=lo utilizando um underline (_)

nome = 'Pedro Lucas'
lista = [1, 2, 3]
numeros = range(1, 10) # temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd + 1):
    num = int(input(f'Informa o {n}/{qtd} valor: '))
    soma = soma + num

print(f'A soma é {soma}')

nome = 'Pedro Lucas'
for letra in nome:
    print(letra, end='')
"""





