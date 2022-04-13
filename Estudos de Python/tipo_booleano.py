"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com Inicial Maiuscula
"""


ativo = True
print(f'O usuario está online - {ativo} \n')

"""

Operações Básicas

"""

# Negação (not):
"""
Fazendo a negação,se o valor booleano for verdadeiro o resultado será falso e 
se for falso o resultado será verdadeiro. Ou seja ,sempre o contrario.
"""
ativo = False
print(f'O usuario está online - {not ativo} \n')

# Ou (or):
"""
É uma operação binaria ou seja, depende de dois valores.
Ou um ou outro devem ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False

"""
logado = False
print(f'O usuario está logado no sistema ? - {ativo or logado} \n')

# E (and):
"""
É uma operação binaria ou seja, depende de dois valores.Ambos os 
valores tem que ser verdadeiro.

True or True -> True
True or False -> False
False or True -> False
False or False -> False

"""


