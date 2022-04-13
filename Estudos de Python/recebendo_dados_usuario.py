"""
- ENTRADA DE DADOS DO USUÁRIO VIA TECLADO
- FORMATAÇÃO DE SAÍDA DE DADOS

input() -> Todo dado recebido via input é do tipo string


"""


# Entrada de Dados
import datetime

# print("Qual seu Nome ?")
# nome = input()  # Entrada de dados
nome = input('Qual Seu Nome? ')

# print("Qual seu idade ?")
# idade = input()
idade = int(input('Qual sua idade? '))

# Saída de Dados

# Exemplo de print 'antigo' 2.X
# print("Seja bem-vindo %s sua idade é %s" % (nome, idade))

# Exemplo de print "moderno" 3.X
# print("Seja Bem-Vindo(a) {0} sua idade é {1}" .format(nome, idade))


# Exemplo de print forma mas atual
print(f"Seja Bem-Vindo {nome} sua idade é {idade}")
print(f'Você Nasceu em {datetime.datetime.now().year - idade}')
