"""
    8 - faça um progrma que leia 2 notas de um aluno,verifique se as notas são validas e
    exiba na tela a média destas notas.Uma nota válida des ser,obrigatoriamente um
    valor entre 0.0 e 10.0,onde caso a nota não possua valor valido,esse fato deve ser
    informado ao usuário e o programa termina.
"""

nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))

if nota1 <= 10 and nota2 <= 10:
    media = (nota1 + nota2) / 2
    print(f'Sua média é de {media}')
else:
    print('Alguns dos números é inválido')
