"""
Listas

Listas em Pytho funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem dinâmicos e também de podermos colocar QUALQUER tipo de dado.

- Dinâmico:
    Não Possue tamanho fixo.Ou seja ,podemos criar a lista e simplesmente ir adicionando elementos;
    Qualquer tipo de dado: Não possuem tipo de dado fimo.OU seja podemos colocar qualquer tipo de dado.

As listas em python são representados por colchetes: []

lista_1 = [1, 99, 4, 27, 15, 1, 5, 6, 88, 9890, 5434, 23, 1, 23, 4, 2]
lista_2 = ['P', 'E', 'D', 'O', ' ', 'L', 'U', 'C', 'A', 'S']
lista_3 = []
lista_4 = list(range(11))
lista_5 = list('Pedro Lucas')

# Podemos  checar se determinado valor está presente na lista
num = 7
if 8 in lista_4:
    print(f'\nEncontrei o Número {num}')
else:
    print(f'\nNão encontrei o Número {num}')

# Podemos  ordenar uma lista (sort)
lista_1.sort()
print('\n', lista_1)

# Podemos contar o número de ocorrencia de um valor em uma lista (count)
print('\n', lista_1.count(1))

# Adicionar elementos em Listas

# Para adicionar elementos em lista,utilizamos a função append

print('\n', lista_1)
lista_1.append(337)
print('\n', lista_1)
# OBS: Com append, nós só conseguimos adicionar um elemento por vez
# lista1.append(55,77,88) # ERRO

lista_1.append([1, 7, 8])  # Coloca a lista como elemento único (sublista)
print('\n', lista_1)

if [1, 7, 8] in lista_1:
    print('\nEncontrei a Lista')
else:
    print('\nNão encontrei a lista')

lista_1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional á lista
print('\n', lista_1)

# Podemos  Inserir um novo elemento na lista indicando a posição na do indice

# Isso não substitui o valor inicial.O mesmo será desloacado para direita da lista.

lista_1.insert(2, 'Novo Elemento')
print(lista_1)

# Podemos juntar duas listas (usando o extend ou ' + ')

lista_1 = lista_1 + lista_2
# lista_1.extend(lista_2)
print(lista_1)

# Podemos facilmente inverter uma lista (reverse)

# Forma 1
lista_1.reverse()
lista_2.reverse()
print(lista_1)
print(lista_2)

# Forma 2
print(lista_1[::-1])
print(lista_2[::-1])

# Copiar uma lista (copy)

lista_6 = lista_2.copy()
print(lista_6)

# Podemos contar quantos elementos existem dentro (len)
print(len(lista_5))

# Podemos  remover o ultimo item de lista (pop)
# OBS: O pop não somente remove o ultimo elemento mas tambem o retorna
print(lista_5)
lista_5.pop()
print(lista_5)

# Podemos remove um elemento pelo indice
# OBS: Os elementos á direita deste indice serão deslocados a esquerda
lista_5.pop(2)
print(lista_5)

# Podemos remover todos os elementos zerar a lista - clear
print(lista_5)
lista_5.clear()
print(lista_5)

# Podemos repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)
# Podemos conerter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrao,o split separa os elementos da lista pelo espaço entre elas

# Exemplo 2
curso = 'Programação,em,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma Lista em uma String
lista_6 = ['Programação', 'em', 'Python:', 'Essencial']

# OBS: Abaixo estamos falando: Pega a lista_6, coloca espaço entre cada elemento e transforma em string
curso = ' '.join(lista_6)
print(curso)

# OBS: Abaixo estamos falando: Pega a lista_6, coloca cifrão entre cada elemento e transforma em string
curso = '$'.join(lista_6)
print(curso)

# Podemos colocar qualquere tipo de dado em uma lista, inclusive misturando esse dados
lista_6 = [1, 2, 'Pedro', 'd', [1, 2, 3]]
print(lista_6)

# Iterando sobre listas

# Exemplo 1 - Utilizando o  For
soma = 0
for elemento in lista_1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando o while

carrinho = []
produto = ''

while produto != 'sair':
    produto = input("Adicione um produto na lista ou digitye 'sair' para sair: ")
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# Utilizando variaveis em uma listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#           0        1        2         3        4
cores = ['Verde', 'Preto', 'Branco', 'Azul', 'Amarelo']

print(cores[0])  # Verde
print(cores[1])  # preto
print(cores[2])  # Branco
print(cores[3])  # Azul
print(cores[4])  # Amarelo

# Fazemos o acesso aos elementos de forma indexada inversa
print(cores[-1])  # Amarelo
print(cores[-2])  # Azul
print(cores[-3])  # Branco
print(cores[-4])  # Preto
print(cores[-5])  # Verde

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

cores = ['Verde', 'Preto', 'Branco', 'Azul', 'Amarelo']

# Gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros metodos não tão importantes mas támbem uteis

# Encontrar o índice de um elemento na lista

numeros = [5, 1, 2, 3, 4, 5, 5, 66, 77, 88, 99]
# Em qual índice da lista está o valor 2?
print(numeros.index(2))

# Em qual índice da lista está o valor 99?
print(numeros.index(99))

# print(numeros.index(19))  # Gera ValueError

# OBS: Caso não tenha esse elemento na lista será apresentado erro ValueError

# OBS: Retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja qual indice começar a buscar
print(numeros.index(5, 1))  # Buscando a partir do indice 1

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(99, 5, 11))  # Buscando o valor 99 entre os indices 5 a 11

# Revisão de slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o parametro inicio

lista = [1, 2, 3, 4]

print(lista[1:])  # Inciando no 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parametro fim

print(lista[:2])  # começa no 0 e pega até o indice 2 - 1
print(lista[:4])  # começa no 0 e pega até o indice 4 - 1
print(lista[1:3])  # começa no 1 e pega até o indice 3 - 1

# Trabalhando com slice de lista com o parametro passo

print(lista[1::2])  # Começa em 1, vai até o final , de 2 em 2

print(lista[::2])  # Começa em 0, vai até o final , de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Geek', 'University']

nomes.reverse()
print(nomes)

# Soma, Valor Máximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # máximo valor
print(min(lista))  # minimo valor
print(len(lista))  # tamanho da lista

# Tranformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um numero diferente de elementos na lista ou variaveis para receber os dados, teremos ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificamos uma lista ,não afeta a outra. isso em Python
#  é chamado de Deep Copy ou (copia profunda)
"""

# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)
nova = lista

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# ápos realizar modificação em uma listas, essa modificação se refletiu em ambas listas.
# Isso em Python é chamado de Shallow Copy.
