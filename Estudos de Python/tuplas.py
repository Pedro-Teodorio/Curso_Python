"""
Tuplas

Tuplas são bastante parecidas com listas

Existem basicamente duas diferenças básicas:

1- As tuplas são representadas por parênteses ()

2- As tuplas são imutyaveis: isso significa que ao criar uma tupla ela não muda. Toda
a operação em uma tupla gera uma nova tupla.

# CUIDADO 1: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento
tupla3 = (4)  # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla

print(tupla4)
print(type(tupla4))

tupla5 = 4,

print(tupla5)
print(type(tupla5))

# CONCLUSÃO: Podemos concluir que uma tupla são definidas pela vírgula e não pelo uso de parênteses

(4) -> Não é Tuplas
(4,) -> É tupla
4, -> É tupla

# Podemos gerar uma tupla dinâmicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)

# Desempacotamento de Tupla
tupla = ('Pedro Lucas', 20, '99681-1376')

nome, idade, telefone = tupla

print(nome)
print(idade)
print(telefone)

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar

# Métodos para adição, remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis

# Soma* ,Valor Máximo*, Valor Minimo e Tamanho
# *Se os valores forem todos inteiros ou reais
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = 1, 2, 3,
print(tupla1)
tupla2 = 4, 5, 6,
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutaveis

tupla1 = tupla1 + tupla2 # Tuplas são imutaveis, mas podemos sobrescrever os seus valores
print(tupla1)

# Verificcar se um determindado valor está dentro de uma tuplas
tupla = 1, 2, 3

print(3 in tupla)

# Iterando sobre uma tuplas
tupla = 1, 2, 3

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(f'{indice} - {valor}')

# Contando elementos dentro de uma tupla
tupla = 'a', 'b', 'c', 'd', 'e', 'a', 'b'
print(tupla.count('a'))

# Dicas na utilização de tuplas
# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1
meses = 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'


# Slicing
# tupla[inicio:fim:passo]

print(meses[5:9])

# O acesso a elementos de uma tupla tambem é semelhante a de uma lista
print(meses[8])

# Iterando com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual indice o elemto está na tupla
print(meses.index('Setembro'))
# OBS: caso o elemento não exista, será gerado ValueError.

# Por que utilizar tuplas

# — Tuplas são mais rápidas do que listas
# — Tuplas deixam o seu código mais seguro*

# *Isso porque trabalhar com elementos imutaveis traz segurança para o código

# Copiando uma tupla para outra

tupla = 1, 2, 3
print(tupla)

nova = tupla  # Na tupla não temos problema de Shallow Copy

print(nova)
print(tupla)

outra = 4, 5, 6

nova = nova + outra

print(nova)
print(tupla)
"""




