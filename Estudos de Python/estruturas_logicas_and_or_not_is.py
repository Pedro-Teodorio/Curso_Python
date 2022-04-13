"""
Estruturass logicas and (e), or (ou) ,not (não) . is(é)

Operadores únarios:
    - not
Operadores bínarios:
    - and,or , is

Regras de Funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor tem que ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True,vira False, se for False vira True
Para o 'is', o valor é comparado com segundo.
"""
ativo = True
logado = True

if ativo and logado:
    print('Welcome User')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu email')
