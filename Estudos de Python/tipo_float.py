"""
Tipo Flot

Tipo Real,decimal

Casas decimais

OBS: O separador de casas decimais é o ponto e não a virgula

"""

# Errado do ponto de vista do float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor), "\n")

# Certo do ponto de vista float
valor = 1.44
print(valor)
# Metodo para saber o valor
print(type(valor), "\n")


# Dupla atribuição

valor1, valor2 = 1, 2
print(f'Valores da Atribuição dupla {valor1} e {valor2} \n')

# Conversão de Float para Int
"""
OBS: Ao converter valores float para inteiro, nós perdemos a precisão
"""
resultado = int(valor)
print(f"Conversão da variavel valor: {resultado} \n")

# Números complexos
"""
OBS: Atribuindo o j na frente do valor
"""
variavel = 5j
print(type(variavel))
