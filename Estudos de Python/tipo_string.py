"""
Tipo String

Em Python, strings é tudo que estiver entre:
- Aspas simples -> 'Pedro Lucas'
- Aspas Duplas -> "Pedro Lucas"
- Aspas Simples Triplas -> '''Pedro Lucas'''
"""
# - Aspas Duplas Triplas -> """ Pedro Lucas """


# upper - Deixa a String toda em Maiusculo
nome = 'pedro lucas'
print(f'deixei tudo em MAIUSCULO {nome.upper()}\n')

# lower - Deixa a String toda em minusculo
print(f'DEIXEI TUDO EM minusculo {nome.lower()}\n')

# Separa a String e tranforma em um vetor de strings
print(f'Transformei em um vetor {nome.split()}\n')

# Slice de String
print('Slice de String Normal')
print(nome[0:5])
print(nome[6:13], '\n')

# Slice de String com split
print('Slice de String Normal com Split')
print(nome.split()[0])
print(nome.split()[1], '\n')


"""
Inversão de um vetor
[::-1] -> Comece do primeiro elemento, vá até  o final e inverta
"""
print('Inverte a String')
print(nome[::-1], "\n")

# replace - substituição de caracteres de uma string
print('Substituição de caracteres')
print(nome.replace(' ', '-'))


