"""
    9 - Leia o sálario de um trabalhador e o valor da prestação de um emprestimo. Se a
    prestação for maior que 20% do salário imprima 'EMPRÉSTIMO NÃO CONCEDIDO'  caso
    contrário imprima : 'EMPRÉSTIMO CONCEDIDO.'
"""

salario = float(input('Digite seu salário: '))
valor_emprestimo = float(input('Valor da prestação que quer pagar no empréstimo: '))

calc_autorizacao_emprestimo = salario * 0.2

if valor_emprestimo > calc_autorizacao_emprestimo:
    print('\nEMPRÉSTIMO NÃO CONCEDIDO')
else:
    print('\nEMPRÉSTIMO  CONCEDIDO')


